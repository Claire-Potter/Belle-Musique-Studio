"""
Customisation user sign up form to ensure first name and last
name are saved so that the fields can be utilised for
customer and subscription creation on stripe

Completed as per the below site:
https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/
"""
from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    """
    The Custom Signup Form ensures that a user completes
    their first name and last name when registering on the site.
    """
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
