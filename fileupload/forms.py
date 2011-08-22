#!/usr/local/bin/python
# coding: utf-8

from fileupload.widgets import MultipleFileInput

from django import forms
class FileUploadSimpleForm(forms.Form):
    file = forms.FileField(widget=MultipleFileInput)
    file_field = 'file'
    add_url_name = 'file_add'
    delete_url_name = 'file_delete'
    media_url = None
    submit_url = None

    def get_file_field(self):
        if not self.file_field:
            self.file_field = 'file'
        return self.file_field
    def get_submit_url(self, *args, **kwargs):
        if not self.submit_url:
            self.submit_url = '#'
        return self.submit_url
    def get_media_url(self, *args, **kwargs):
        if not self.media_url:
            self.media_url = 'uploaded'
        return self.media_url
    def get_delete_url_name(self, *args, **kwargs):
        if not self.delete_url_name:
            self.delete_url_name = 'file_delete'
        return self.delete_url_name