from django import forms 
from .models import RegisterData
class RegisterForm(forms.ModelForm):

	class Meta:
		model  = RegisterData
		fields = ["name","contact","address","email","password"]
		widgets={
		"password":forms.PasswordInput
		}

	# def clean_contact(self):
	# 	contact = str(self.cleaned_data['contact'])
	# 	if len(contact) < 10:
	# 		raise forms.ValidationError('Mobile Number Should Contain minimum 10 characters')
	# 	return contact


class LoginForm(forms.Form):
	Userid = forms.EmailField(required=True,label="User Name")
	Password = forms.CharField(label='Password',widget=forms.PasswordInput)
