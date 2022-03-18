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


class LessonPriceForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Plan
        fields = ('id', 'amount', 'currency', 'interval', 'nickname', 'usage_type', 'trial_period_days')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['readonly'] = True
        self.fields['amount'].widget.attrs['readonly'] = True
        self.fields['currency'].widget.attrs['readonly'] = True
        self.fields['interval'].widget.attrs['readonly'] = True
        self.fields['usage_type'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


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
            'currency': 'gbp',
            'interval': 'A URL of a publicly-accessible image address.',
            'nickname': 'The alt text for the image',
            'usage_type': 'Appears on your customer\'s credit card statement',
            'trial_period_days': 'Billed unit title eg: lesson',
        }
        for field in self.fields:
            if field not in ('active', ):
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder 
        
        self.fields['active'].initial = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
