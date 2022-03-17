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
        products = Product.objects.all()
        product_names = [(p.id, p.name ) for p in products]

        self.fields['name'].choices = product_names
        self.fields['id'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class LessonPriceForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Plan
        fields = ('id', 'amount', 'currency', 'interval', 'nickname', 'usage_type')


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
        products = Product.objects.all()
        product_names = [(p.id, p.name ) for p in products]

        self.fields['name'].choices = product_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class LessonPriceAddForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Plan
        fields = ('amount', 'currency', 'interval', 'nickname', 'usage_type', 'active')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['active'].initial = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
