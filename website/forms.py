# forms.py
from django import forms


class PartnerForm(forms.Form):
    name = forms.CharField(max_length=100)
    school_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    mobile_or_wechat = forms.CharField(max_length=100, required=False)
    help_description = forms.CharField(widget=forms.Textarea, required=False)
