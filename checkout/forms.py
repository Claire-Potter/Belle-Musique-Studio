"""
Forms created for the Belle Musique Studio
Checkout application.

OrderForm set up to enable a user to capture address details
to be used to place an order
with the Music Store. It will be saved
to the Order model.

SubscribedCustomerForm set up to enable a user to submit
their details. Customer created through DJStripe,
details are added  and saved to the SubscribedCustomerForm.

SubscriptionLineItemForm set up to enable a user to submit
subscription details. Subscription created through DJStripe,
details are added  and saved to the SubscriptionLineItem model.
"""
from django import forms
# Forms are imported from Django
from .models import Order, SubscribedCustomer, SubscriptionLineItem
# Models are imported from models.py


class OrderForm(forms.ModelForm):
    """
    Form set up to enable a user to capture address details
    to be used to place an order
    with the Music Store. It will be saved
    to the Order model.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field not in ('country', 'full_name', 'email'):
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class SubscribedCustomerForm(forms.ModelForm):
    """
    SubscribedCustomerForm set up to enable a user to submit
    their details. Customer created through DJStripe,
    details are added  and saved to the SubscribedCustomerForm.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = SubscribedCustomer
        fields = ('full_name', 'email', 'phone_number',
                 'country' )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone Number'}

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'phone_number':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class SubscriptionLineItemForm(forms.ModelForm):
    """
    SubscriptionLineItemForm set up to enable a user to submit
    subscription details. Subscription created through DJStripe,
    details are added  and saved to the SubscriptionLineItem mode.
    """
    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = SubscriptionLineItem
        fields = ('student',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'student': 'Student Full Name',}

        for field in self.fields:
            if field  == ('student'):
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
