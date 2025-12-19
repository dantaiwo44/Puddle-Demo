from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'category': forms.Select(attrs=
             {'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs=
                {'class': INPUT_CLASSES,
                'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs=
                {'class': INPUT_CLASSES,
                 'placeholder': 'Item Description',}),
            'price': forms.NumberInput(attrs=
                {'class': INPUT_CLASSES,}),
            'image': forms.ClearableFileInput(attrs=
                {'class': INPUT_CLASSES,}), }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_sold']
        widgets = {
           
            'name': forms.TextInput(attrs=
                {'class': INPUT_CLASSES,
                'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs=
                {'class': INPUT_CLASSES,
                 'placeholder': 'Item Description',}),
            'price': forms.NumberInput(attrs=
                {'class': INPUT_CLASSES,}),
            'image': forms.ClearableFileInput(attrs=
                {'class': INPUT_CLASSES,}), }