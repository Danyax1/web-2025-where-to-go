# places/forms.py
from django import forms

class PlaceForm(forms.Form):
    name = forms.CharField(
        label="Назва",
        min_length=1,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        label="Опис",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    location = forms.CharField(
        label="Локація",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    rating = forms.IntegerField(
        label="Рейтинг",
        min_value=1,
        max_value=5,
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
