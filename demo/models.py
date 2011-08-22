from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)

class NoteAttachment(models.Model):
    file = models.FileField(upload_to='attachments')

