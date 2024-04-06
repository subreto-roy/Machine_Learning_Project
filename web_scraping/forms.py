# forms.py in your extractor app

from django import forms

class SchemaForm(forms.Form):
    name = forms.CharField(required=False)
    author = forms.CharField(required=False)
    format = forms.CharField(required=False)
    # Add more fields as necessary
