"""
Forms created for the Xperience DezignWiz
Home application.
ContactForm set up to enable a user to create
a contact message and save it. It will
be sent to the admin account and saved
to the Contact model.
"""
from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """
     Form set up to enable a user to create
     a contact message and save it. It will
     be sent to the admin account and saved
     to the Contact model. It can be accessed
     via the admin pane.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = Contact
        fields = ('name', 'email', 'body',)
