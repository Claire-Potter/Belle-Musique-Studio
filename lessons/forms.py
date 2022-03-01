"""
Forms created for the Xperience DezignWiz
Home application.
ContactForm set up to enable a user to create
a contact message and save it. It will
be sent to the admin account and saved
to the Contact model.
"""
from django import forms
from .models import SubscribedUser


class SubscriptionForm(forms.ModelForm):
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
        model = SubscribedUser
        fields = ('full_name', 'email', 'lesson', 'subscription_type', 'quantity')


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'lesson': 'Lesson Type',
            'subscription_type': 'Subscription',
            'quantity': 'Number of Subscriptions'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
