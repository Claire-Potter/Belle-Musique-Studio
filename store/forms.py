"""
Forms created for the Belle Musique Studio
Store application.

ProductForm set up to enable a staff member to create
a new product or edit an existing product.
"""
from django import forms
# Forms are imported from Django

from .models import Category, MusicProduct
# Models are imported from models.py
from .widgets import CustomClearableFileInput
# Widget is imported from widget.py


class ProductForm(forms.ModelForm):
    """
    ProductForm set up to enable a staff member to create
    a new product or edit an existing product.
    """

    class Meta:
        """
        Meta added to identify the model utilised by
        the form and the fields which the form needs
        to include for the user to edit.
        """
        model = MusicProduct
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        call_names = [(c.id, c.get_call_name()) for c in categories]

        self.fields['category'].choices = call_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
