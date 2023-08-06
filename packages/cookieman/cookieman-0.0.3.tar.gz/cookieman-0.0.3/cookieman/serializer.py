"""Cookieman serializer submodule."""

import zlib
import base64

try:
    import typing
except ImportError:
    pass

import msgpack
import itsdangerous


class CookieManSerializer(object):
    """
    Signed compressed session cookie serializer.

    This class implements the following:

    - Messagepack python object serialization.
    - Signature check using itsdangerous.TimestampSigner.
    - Compression using python's standard zlib.
    - URL-safe base64 encoding (to http header issues).

    """

    signer_class = itsdangerous.TimestampSigner

    def __init__(self, secret, salt):  # type: (str, str) -> None
        """
        Initialize.

        :param secret: itsdangerous signer secret
        :param salt: itsdangerous signer salt
        """
        self.signer = self.signer_class(secret, salt=salt)

    def dumps(self, data):  # type: (typing.Any) -> bytes
        """
        Get serialized representation of given object.

        :param data: serializable object
        :return: serialized data
        """
        dumped = msgpack.packb(data, use_bin_type=True)
        signed = self.signer.sign(dumped)
        compressed = zlib.compress(signed)
        return base64.urlsafe_b64encode(compressed)

    def loads(self,
              data,  # type: bytes
              max_age=None,  # type: typing.Optional[int]
              ):  # type: (...) -> typing.Any
        """
        Get object from serialized data.

        :param data: serialized data
        :return: unserialized object
        """
        decoded = base64.urlsafe_b64decode(data)
        decompressed = zlib.decompress(decoded)
        signed = self.signer.unsign(decompressed, max_age=max_age)
        return msgpack.unpackb(signed, raw=False)
