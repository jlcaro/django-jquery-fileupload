from django.db import models

class FileUploadData(object):
    def __init__(self, name, url, delete_url=None, delete_type='DELETE'):
        self.name = name
        self.url = url
        self.delete_url = delete_url
        self.delete_type = delete_type