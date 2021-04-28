import os

from minimalkv.contrib import ExtendedKeyspaceMixin
from minimalkv.fs import FilesystemStore
from minimalkv.memory import DictStore
from minimalkv.memory.redisstore import RedisStore
from minimalkv.net.azurestore import AzureBlockBlobStore
from minimalkv.net.botostore import BotoStore
from minimalkv.net.gcstore import GoogleCloudStore


class HDictStore(ExtendedKeyspaceMixin, DictStore):
    pass


class HRedisStore(ExtendedKeyspaceMixin, RedisStore):
    pass


class HAzureBlockBlobStore(ExtendedKeyspaceMixin, AzureBlockBlobStore):
    pass


class HBotoStore(ExtendedKeyspaceMixin, BotoStore):
    def size(self, key: str) -> bytes:
        """Get size of data at key in bytes.

        Parameters
        ----------
        key : str
            Key of data.

        Returns
        -------
        size : int
            Size of value at key in bytes.
        """
        k = self.bucket.lookup(self.prefix + key)
        return k.size


class HGoogleCloudStore(ExtendedKeyspaceMixin, GoogleCloudStore):
    pass


class HFilesystemStore(ExtendedKeyspaceMixin, FilesystemStore):
    def size(self, key: str) -> int:
        """Get size of data at key in bytes.

        Parameters
        ----------
        key : str
            Key of data.

        Returns
        -------
        size : int
            Size of value at key in bytes.
        """
        return os.path.getsize(self._build_filename(key))