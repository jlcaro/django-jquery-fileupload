
from django.forms.util import flatatt
from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe

class MultipleFileInput(ClearableFileInput):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        return mark_safe(u'<input%s multiple/>' % flatatt(final_attrs))