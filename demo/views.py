from django.conf.urls.defaults import *

from demo import models
from django.views.generic import CreateView, DeleteView

from django.http import HttpResponse
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.conf import settings

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"


class FileCreateView(CreateView):
    model = models.NoteAttachment
    
    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('file')
        data = [{
            'name': f.name,
            'url': settings.MEDIA_URL + "pictures/" + f.name,
            #'thumbnail_url': settings.MEDIA_URL + "pictures/" + f.name,
            'delete_url': reverse('upload-delete', args=[self.object.id]),
            'delete_type': "DELETE"
        }]
        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=file.json'
        return response


class FileDeleteView(DeleteView):
    model = models.NoteAttachment

    def delete(self, request, *args, **kwargs):
        """
        This does not actually delete the file, only the database record.  But
        that is easy to implement.
        """
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class JSONResponse(HttpResponse):
    """ JSON Response class."""
    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = simplejson.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)