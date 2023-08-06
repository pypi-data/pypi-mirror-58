import json
from io import SEEK_END
from eve.io.media import MediaStorage
from flask.app import Flask
from flask import current_app
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists, NoSuchKey)
from bson.objectid import ObjectId
from eve_s3storage.s3_file import S3File


class S3MediaStorage(MediaStorage):
    """
    MediaStorage implementation compatible with AWS S3 service.
    """
    def __init__(self, app=None):
        """
        :param app: the flask application (eve itself). This can be used by
        the class to access, amongst other things, the app.config object to
        retrieve class-specific settings.
        """
        super(S3MediaStorage, self).__init__(app)

        self.validate()

        self.bucket = app.config['S3_BUCKET']
        self.host = app.config['S3_HOST']
        self.access_key = app.config['S3_ACCESS_KEY']
        self.secret_key = app.config['S3_SECRET_KEY']
        self.secure_connection = app.config.get('S3_SECURE_CONNECTION', True)

        self.minio = Minio(self.host,
                  access_key=self.access_key,
                  secret_key=self.secret_key,
                  secure=self.secure_connection)
        self.prepare_bucket(self.bucket)


    def validate(self):
        """ Make sure that the application is an eve application.
        instance.
        """
        if self.app is None:
            raise TypeError('Application object cannot be None')

        if not isinstance(self.app, Flask):
            raise TypeError('Application object must be a Eve application')


    def prepare_bucket(self, bucket):
        try:
            self.minio.make_bucket(bucket)
        except BucketAlreadyOwnedByYou as err:
            pass
        except BucketAlreadyExists as err:
            pass
        except ResponseError as err:
            raise


    def exists(self, id_or_filename, resource=None):
        try:
            self.minio.get_object(self.bucket, str(id_or_filename))
        except ResponseError:
            return False
        except NoSuchKey:
            return False
        return True


    def get(self, id_or_filename, resource=None):
        try:
            object_name = str(id_or_filename)
            metadata = self.minio.stat_object(self.bucket, object_name)
            data = self.minio.get_object(self.bucket, object_name)
        except NoSuchKey:
            return None

        return S3File(metadata, data)


    def delete(self, id_or_filename, resource=None):
        return self.minio.remove_object(self.bucket, str(id_or_filename))


    def put(self, content, filename=None, content_type=None, resource=None):
        _id = str(ObjectId())
        size = content.getbuffer().nbytes
        self.minio.put_object(self.bucket, _id, content, size, content_type, metadata={'filename': filename})
        return _id
