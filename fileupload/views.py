from django.conf.urls.defaults import *

from django.views.generic import CreateView, DeleteView, FormView

from django.http import HttpResponse
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.conf import settings

from fileupload.models import FileUploadData

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

class FileFormAddView(FormView):
    initial = {}
    form_class = None
    success_url = None

    def form_valid(self, form):
        f = self.request.FILES.get(form.get_file_field())
        args_id = self.handle_uploaded_file(f, form)
        data = FileUploadData(
            name = f.name,
            url = settings.MEDIA_URL + form.get_media_url() + '/' + f.name,
            delete_url = reverse(form.get_delete_url_name(), args=args_id),
        )
        response = JSONResponse([data.__dict__], {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=file.json'
        return response
    def form_invalid(self, form):
        return super(FileFormAddView, self).form_invalid(form)
    def get_initials_from_request(self):
        d = {}
        for k in self.kwargs:
            d[k] = self.kwargs[k]
        return d
    def handle_uploaded_file(self, file, form, *args, **kwargs):
        return None
    def get_url_id_args(self, *args, **kwargs):
        return args

class FileDeleteView(DeleteView):
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

class FileCreateView(CreateView):
    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('file')

class JSONResponse(HttpResponse):
    """ JSON Response class."""
    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = simplejson.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)