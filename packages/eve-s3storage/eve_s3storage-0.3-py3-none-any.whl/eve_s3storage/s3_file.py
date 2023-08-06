from datetime import datetime
from time import mktime
from io import BytesIO
import urllib3


class S3File(BytesIO):
    def __init__(self, metadata: object, data: urllib3.response.HTTPResponse):        
        BytesIO.__init__(self, data.read())
        self.metadata = metadata
        self.content_type = metadata.content_type
        self.upload_date = datetime.fromtimestamp(mktime(metadata.last_modified))
        self.size = metadata.size
        self.length = self.size
        self.filename = metadata.metadata['X-Amz-Meta-Filename']
