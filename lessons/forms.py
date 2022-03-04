""".git/"""
from django import forms

from .models import Type, Lesson
from .widgets import CustomClearableFileInput


class LessonForm(forms.ModelForm):
    """.git/"""

    class Meta:
        """.git/"""
        model = Lesson
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types = Type.objects.all()
        call_names = [(t.id, t.get_call_name()) for t in types]

        self.fields['types'].choices = call_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
