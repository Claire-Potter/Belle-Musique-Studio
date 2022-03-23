"""
Forms created for the Belle Musique Studio
Home application.

ContactForm set up to enable a user to create
a contact message and save it. It will
be sent to the admin account and saved
to the Contact model.

StudentShowcaseForm set up to enable a staff user to create
a student record to be showcased and save it. It will
be sent to the admin account and saved
to the StudentShowcase model.
"""
from django import forms
# Forms are imported from Django
from .models import Contact, StudentShowcase
# Models are imported from models.py


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


class StudentShowcaseForm(forms.ModelForm):
    """
     StudentShowcaseForm set up to enable a staff user to create
     a student record to be showcased and save it. It will
     be sent to the admin account and saved
     to the StudentShowcase model. Accessed via the Add Student Showcase
     page on the front end or from within Site Admin. The latest record
     is displayed on the about page.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = StudentShowcase
        fields = '__all__'
