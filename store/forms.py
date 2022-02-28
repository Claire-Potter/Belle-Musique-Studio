from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
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