from django import forms
from healthapp.models import contactModel,userModel

class registerForm(forms.ModelForm):
    class Meta():
        model = userModel
        fields =['first_name','last_name','email','password','phone']