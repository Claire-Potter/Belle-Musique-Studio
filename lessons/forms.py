""".git/"""
from django import forms

from djstripe.models import Product
from .widgets import CustomClearableFileInput


class LessonProductForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Product
        fields = ('name', 'description', 'url', 'caption', 'statement_descriptor', 'unit_label',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        products = Product.objects.all()
        product_names = [(p.id, p.name) for p in products]

        self.fields['name'].choices = product_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
