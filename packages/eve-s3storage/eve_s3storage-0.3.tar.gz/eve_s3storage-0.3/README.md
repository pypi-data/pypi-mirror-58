# eve-s3storage

Python Eve allows to use different file storage backends.
This package adds support for S3/Minio file storage.

The python library minio is used. This allows to use other
cloud storage providers with a minio service in between.

## Installation

```sh
pip install eve_s3storage
```

## Usage

Set the following configuration values (in the flask/eve configuration object):

Initialize the Python Eve app in the following way:


| Configuration Key    | Example value    | Description                         |
|----------------------|------------------|-------------------------------------|
| S3_HOST              | `localhost:9000` | Server address of the minio service |
| S3_ACCESS_KEY        | `minio_access`   | Access key ID for authentication    |
| S3_SECRET_KEY        | `minio_secret`   | Secret key for authentication       |
| S3_BUCKET            | `test`           | S3 bucket                           |
| S3_SECURE_CONNECTION | `True`           | Specifies whether to connect to the minio service using HTTPS (`True`) or HTTP (`False`) |

```python
from eve_s3storage import S3MediaStorage

config = {
  # other configuration values here
  'S3_HOST': 'localhost:9000',
  'S3_ACCESS_KEY': 'minio_access',
  'S3_SECRET_KEY': 'minio_secret',
  'S3_BUCKET': 'testbucket',
  'S3_SECURE_CONNECTION': False,
}

app = eve.Eve(settings=config, media=S3MediaStorage)
```
