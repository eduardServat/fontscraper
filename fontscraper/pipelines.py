import hashlib

from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.python import to_bytes


class FontscraperPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f'full/{media_guid}.zip'
