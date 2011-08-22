from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def form_submit_url(context):
    return "%s" % context['form'].get_submit_url()

@register.simple_tag(takes_context=True)
def form_file_fieldname(context):
    return context['form'].get_file_field()
