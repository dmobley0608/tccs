from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label="Name" ,max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    phone_number = forms.CharField(label="Phone Number", max_length=11, required=False)
    message = forms.CharField(widget=forms.Textarea)