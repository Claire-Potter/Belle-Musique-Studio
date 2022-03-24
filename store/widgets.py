"""
Belle Musique Studio widgets configuration

Definitions from https://www.fullstackpython.com
unless stated otherwise.
"""
from django.forms.widgets import ClearableFileInput
#A widget is Django’s representation of an HTML input element.
# The widget handles the rendering of the HTML, and the extraction
# of data from a GET/POST dictionary that corresponds to the widget.
# https://docs.djangoproject.com/en/4.0/ref/forms/widgets/

from django.utils.translation import gettext_lazy as _
# gettext_lazy is a callable within the
# django.utils.translation module of the Django project.

class CustomClearableFileInput(ClearableFileInput):
    """
    Widget created to clear the image field
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'custom_widget_templates/custom_clearable_file_input.html'
