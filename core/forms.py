from django import forms
from .models import shoppingtrends

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField()