"""
Forms created for the Belle Musique Studio
Profile application.

The UserProfile  form allows the user to add,
edit and delete the various userprofile fields.

Created as per the Code Institute 'Boutique Ado' project.
"""
from django import forms
# Forms are imported from Django

from .models import UserProfile
# Model imported from models.py


class UserProfileForm(forms.ModelForm):
    """
    The UserProfile  form allows the user to add,
    edit and delete the various userprofile fields.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_additional_email': 'Additional Email Address',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field not in ('default_country',):
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input smallest-text'
            self.fields[field].label = False
