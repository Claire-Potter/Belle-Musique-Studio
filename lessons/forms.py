""".git/"""
from django import forms

from djstripe.models import Product, Plan


class LessonProductForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Product
        fields = ('id', 'name', 'description', 'url', 'caption',
                  'statement_descriptor', 'unit_label',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

        self.fields['name'].widget.attrs['cols'] = "20"
        self.fields['description'].widget.attrs['cols'] = "20"
        self.fields['caption'].widget.attrs['cols'] = "20"
        self.fields['name'].widget.attrs['rows'] = "2"
        self.fields['description'].widget.attrs['rows'] = "2"
        self.fields['caption'].widget.attrs['rows'] = "2"


class LessonPriceForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Plan
        fields = ('id', 'amount', 'currency', 'interval',
                   'nickname', 'usage_type', 'trial_period_days')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['readonly'] = True
        self.fields['amount'].widget.attrs['readonly'] = True
        self.fields['currency'].widget.attrs['readonly'] = True
        self.fields['interval'].widget.attrs['readonly'] = True
        self.fields['usage_type'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

        self.fields['nickname'].widget.attrs['cols'] = "20"
        self.fields['nickname'].widget.attrs['rows'] = "2"
        self.fields['interval'].widget.attrs['style'] = 'width:250px'
        self.fields['usage_type'].widget.attrs['style'] = 'width:250px'


class LessonProductAddForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Product
        fields = ('name', 'description', 'url', 'caption',
                  'statement_descriptor', 'unit_label',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'The product\'s name, meant to be displayable to the customer.',
            'description': 'A description of this object.',
            'url': 'A URL of a publicly-accessible image address.',
            'caption': 'The alt text for the image.',
            'statement_descriptor': 'Appears on your customer\'s credit card statement.',
            'unit_label': 'Billed unit title eg: lesson.',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

        self.fields['name'].widget.attrs['cols'] = "20"
        self.fields['description'].widget.attrs['cols'] = "20"
        self.fields['caption'].widget.attrs['cols'] = "20"
        self.fields['name'].widget.attrs['rows'] = "2"
        self.fields['description'].widget.attrs['rows'] = "2"
        self.fields['caption'].widget.attrs['rows'] = "2"


class LessonPriceAddForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Plan
        fields = ('amount', 'currency', 'interval', 'nickname',
        'usage_type', 'active', 'trial_period_days')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'amount': 'Amount (as decimal) to be charged on the interval specified.',
            'currency': 'Three letter ISO currency code eg: gbp',
            'nickname': 'A brief description of the plan, hidden from customers.',
            'usage_type': 'Configures how the quantity per period should be determined.',
        }
        for field in self.fields:
            if field not in ('active', 'usage_type', 'trial_period_days', 'interval' ):
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

        self.fields['active'].initial = True
        self.fields['interval'].widget.attrs['readonly'] = True
        self.fields['trial_period_days'].widget.attrs['readonly'] = True
        self.fields['nickname'].widget.attrs['cols'] = "20"
        self.fields['nickname'].widget.attrs['rows'] = "2"
        self.fields['interval'].widget.attrs['style'] = 'width:250px'
        self.fields['usage_type'].widget.attrs['style'] = 'width:250px'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
