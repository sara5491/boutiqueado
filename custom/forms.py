from django import forms
from .models import Custom


class CustomForm(forms.ModelForm):
    class Meta:
        model = Custom
        fields = ['name', 'email', 'message']


    def __init__(self, *args, **kwargs):
        """ Add placeholder text """

        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Your name',
            'email': 'Email Address',
            'message': 'Get in touch',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-0'