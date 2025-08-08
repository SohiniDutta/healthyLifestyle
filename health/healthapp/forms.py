from django import forms
from healthapp.models import contactModel,userModel

class registerForm(forms.ModelForm):
    class Meta():
        model = userModel
        fields =['first_name','last_name','email','password','phone']

class promptForm(forms.Form):
    prompt = forms.CharField(label='Enter Text',max_length=100)
    