from django import forms
from .models import MarchantModel,Product_Model
class MarchantForm(forms.ModelForm):
	class Meta:
		models = MarchantModel
		fields = ['email','password']

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product_Model
		fields = "__all__"