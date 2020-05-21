from django import forms

class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField(max_length=80)
    to=forms.EmailField(max_length=80)
    comment=forms.CharField(required=False,
            widget=forms.Textarea)
