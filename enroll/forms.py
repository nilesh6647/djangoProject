from django import forms
class advisorRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    