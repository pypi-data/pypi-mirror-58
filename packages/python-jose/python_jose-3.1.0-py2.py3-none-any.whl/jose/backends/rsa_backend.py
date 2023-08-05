import binascii

import six
from pyasn1.error import PyAsn1Error

import rsa as pyrsa
import rsa.pem as pyrsa_pem

from jose.backends.base import Key
from jose.backends._asn1 import (
    rsa_private_key_pkcs1_to_pkcs8,
    rsa_private_key_pkcs8_to_pkcs1,
    rsa_public_key_pkcs1_to_pkcs8,
)
from jose.constants import ALGORITHMS
from jose.exceptions import JWKError
from jose.utils import base64_to_long, long_to_base64


LEGACY_INVALID_PKCS8_RSA_HEADER = binascii.unhexlify(
    "30"  # sequence
    "8204BD"  # DER-encoded sequence contents length of 1213 bytes -- INCORRECT STATIC LENGTH
    "020100"  # integer: 0 -- Version
    "30"  # sequence
    "0D"  # DER-encoded sequence contents length of 13 bytes -- PrivateKeyAlgorithmIdentifier
    "06092A864886F70D010101"  # OID -- rsaEncryption
    "0500"  # NULL -- parameters
)
ASN1_SEQUENCE_ID = binascii.unhexlify("30")
RSA_ENCRYPTION_ASN1_OID = "1.2.840.113549.1.1.1"

# Functions gcd and rsa_recover_prime_factors were copied from cryptography 1.9
# to enable pure python rsa module to be in compliance with section 6.3.1 of RFC7518
# which requires only private exponent (d) for private key.


def _gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, (a % b)
    return a


# Controls the number of iterations rsa_recover_prime_factors will perform
# to obtain the prime factors. Each iteration increments by 2 so the actual
# maximum attempts is half this number.
_MAX_RECOVERY_ATTEMPTS = 1000


def _rsa_recover_prime_factors(n, e, d):
    """
    Compute factors p and q from the private exponent d. We assume that n has
    no more than two factors. This function is adapted from code in PyCrypto.
    """
    # See 8.2.2(i) in Handbook of Applied Cryptography.
    ktot = d * e - 1
    # The quantity d*e-1 is a multiple of phi(n), even,
    # and can be represented as t*2^s.
    t = ktot
    while t % 2 == 0:
        t = t // 2
    # Cycle through all multiplicative inverses in Zn.
    # The algorithm is non-deterministic, but there is a 50% chance
    # any candidate a leads to successful factoring.
    # See "Digitalized Signatures and Public Key Functions as Intractable
    # as Factorization", M. Rabin, 1979
    spotted = False
    a = 2
    while not spotted and a < _MAX_RECOVERY_ATTEMPTS:
        k = t
        # Cycle through all values a^{t*2^i}=a^k
        while k < ktot:
            cand = pow(a, k, n)
            # Check if a^k is a non-trivial root of unity (mod n)
            if cand != 1 and cand != (n - 1) and pow(cand, 2, n) == 1:
                # We have found a number such that (cand-1)(cand+1)=0 (mod n).
                # Either of the terms divides n.
                p = _gcd(cand + 1, n)
                spotted = True
                break
            k *= 2
        # This value was not any good... let's try another!
        a += 2
    if not spotted:
        raise ValueError("Unable to compute factors p and q from exponent d.")
    # Found !
    q, r = divmod(n, p)
    assert r == 0
    p, q = sorted((p, q), reverse=True)
    return (p, q)


def pem_to_spki(pem, fmt='PKCS8'):
    key = RSAKey(pem, ALGORITHMS.RS256)
    return key.to_pem(fmt)


def _legacy_private_key_pkcs8_to_pkcs1(pkcs8_key):
    """Legacy RSA private key PKCS8-to-PKCS1 conversion.

    .. warning::

        This is incorrect parsing and only works because the legacy PKCS1-to-PKCS8
        encoding was also incorrect.
    """
    # Only allow this processing if the prefix matches
    # AND the following byte indicates an ASN1 sequence,
    # as we would expect with the legacy encoding.
    if not pkcs8_key.startswith(LEGACY_INVALID_PKCS8_RSA_HEADER + ASN1_SEQUENCE_ID):
        raise ValueError("Invalid private key encoding")

    return pkcs8_key[len(LEGACY_INVALID_PKCS8_RSA_HEADER):]


class RSAKey(Key):
    SHA256 = 'SHA-256'
    SHA384 = 'SHA-384'
    SHA512 = 'SHA-512'

    def __init__(self, key, algorithm):
        if algorithm not in ALGORITHMS.RSA:
            raise JWKError('hash_alg: %s is not a valid hash algorithm' % algorithm)

        self.hash_alg = {
            ALGORITHMS.RS256: self.SHA256,
            ALGORITHMS.RS384: self.SHA384,
            ALGORITHMS.RS512: self.SHA512
        }.get(algorithm)
        self._algorithm = algorithm

        if isinstance(key, dict):
            self._prepared_key = self._process_jwk(key)
            return

        if isinstance(key, (pyrsa.PublicKey, pyrsa.PrivateKey)):
            self._prepared_key = key
            return

        if isinstance(key, six.string_types):
            key = key.encode('utf-8')

        if isinstance(key, six.binary_type):
            try:
                self._prepared_key = pyrsa.PublicKey.load_pkcs1(key)
            except ValueError:
                try:
                    self._prepared_key = pyrsa.PublicKey.load_pkcs1_openssl_pem(key)
                except ValueError:
                    try:
                        self._prepared_key = pyrsa.PrivateKey.load_pkcs1(key)
                    except ValueError:
                        try:
                            der = pyrsa_pem.load_pem(key, b'PRIVATE KEY')
                            try:
                                pkcs1_key = rsa_private_key_pkcs8_to_pkcs1(der)
                            except PyAsn1Error:
                                # If the key was encoded using the old, invalid,
                                # encoding then pyasn1 will throw an error attempting
                                # to parse the key.
                                pkcs1_key = _legacy_private_key_pkcs8_to_pkcs1(der)
                            self._prepared_key = pyrsa.PrivateKey.load_pkcs1(pkcs1_key, format="DER")
                        except ValueError as e:
                            raise JWKError(e)
            return
        raise JWKError('Unable to parse an RSA_JWK from key: %s' % key)

    def _process_jwk(self, jwk_dict):
        if not jwk_dict.get('kty') == 'RSA':
            raise JWKError("Incorrect key type.  Expected: 'RSA', Recieved: %s" % jwk_dict.get('kty'))

        e = base64_to_long(jwk_dict.get('e'))
        n = base64_to_long(jwk_dict.get('n'))

        if 'd' not in jwk_dict:
            return pyrsa.PublicKey(e=e, n=n)
        else:
            d = base64_to_long(jwk_dict.get('d'))
            extra_params = ['p', 'q', 'dp', 'dq', 'qi']

            if any(k in jwk_dict for k in extra_params):
                # Precomputed private key parameters are available.
                if not all(k in jwk_dict for k in extra_params):
                    # These values must be present when 'p' is according to
                    # Section 6.3.2 of RFC7518, so if they are not we raise
                    # an error.
                    raise JWKError('Precomputed private key parameters are incomplete.')

                p = base64_to_long(jwk_dict['p'])
                q = base64_to_long(jwk_dict['q'])
                return pyrsa.PrivateKey(e=e, n=n, d=d, p=p, q=q)
            else:
                p, q = _rsa_recover_prime_factors(n, e, d)
                return pyrsa.PrivateKey(n=n, e=e, d=d, p=p, q=q)

    def sign(self, msg):
        return pyrsa.sign(msg, self._prepared_key, self.hash_alg)

    def verify(self, msg, sig):
        try:
            pyrsa.verify(msg, sig, self._prepared_key)
            return True
        except pyrsa.pkcs1.VerificationError:
            return False

    def is_public(self):
        return isinstance(self._prepared_key, pyrsa.PublicKey)

    def public_key(self):
        if isinstance(self._prepared_key, pyrsa.PublicKey):
            return self
        return self.__class__(pyrsa.PublicKey(n=self._prepared_key.n, e=self._prepared_key.e), self._algorithm)

    def to_pem(self, pem_format='PKCS8'):

        if isinstance(self._prepared_key, pyrsa.PrivateKey):
            der = self._prepared_key.save_pkcs1(format='DER')
            if pem_format == 'PKCS8':
                pkcs8_der = rsa_private_key_pkcs1_to_pkcs8(der)
                pem = pyrsa_pem.save_pem(pkcs8_der, pem_marker='PRIVATE KEY')
            elif pem_format == 'PKCS1':
                pem = pyrsa_pem.save_pem(der, pem_marker='RSA PRIVATE KEY')
            else:
                raise ValueError("Invalid pem format specified: %r" % (pem_format,))
        else:
            if pem_format == 'PKCS8':
                pkcs1_der = self._prepared_key.save_pkcs1(format="DER")
                pkcs8_der = rsa_public_key_pkcs1_to_pkcs8(pkcs1_der)
                pem = pyrsa_pem.save_pem(pkcs8_der, pem_marker='PUBLIC KEY')
            elif pem_format == 'PKCS1':
                der = self._prepared_key.save_pkcs1(format='DER')
                pem = pyrsa_pem.save_pem(der, pem_marker='RSA PUBLIC KEY')
            else:
                raise ValueError("Invalid pem format specified: %r" % (pem_format,))
        return pem

    def to_dict(self):
        if not self.is_public():
            public_key = self.public_key()._prepared_key
        else:
            public_key = self._prepared_key

        data = {
            'alg': self._algorithm,
            'kty': 'RSA',
            'n': long_to_base64(public_key.n),
            'e': long_to_base64(public_key.e),
        }

        if not self.is_public():
            data.update({
                'd': long_to_base64(self._prepared_key.d),
                'p': long_to_base64(self._prepared_key.p),
                'q': long_to_base64(self._prepared_key.q),
                'dp': long_to_base64(self._prepared_key.exp1),
                'dq': long_to_base64(self._prepared_key.exp2),
                'qi': long_to_base64(self._prepared_key.coef),
            })

        return data
