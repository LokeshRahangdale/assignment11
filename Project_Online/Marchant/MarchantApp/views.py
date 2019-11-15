from django.shortcuts import render
import json
import requests
from django.http import HttpResponse

# Create your views here.
def ShowIndex(request):
	return render(request,"login.html")

def MarchantLogin(request):
	username = request.POST['uname']
	password = request.POST['password']
	d1 = {
	"uname" : username,
	"upass" : password
	}
	json_data = json.dumps(d1)
	try:
		resp = requests.post("http://127.0.0.1:8000/marchant_login/",data=json_data)
		if resp:
			return render(request,"menu.html")
		else:
			return render(request,"login.html",{"massage":"Invalid rediantials"})
	except requests.exceptions.ConnectionError:
		return render(request,"login.html",{"massage":"Server Not Available"})

def AddProductPage(request):
	return render(request,"addproduct.html")
from django.views.generic import View
class SaveProduct(View):
	def post(self,request):
		pno = request.POST['pno']
		pname = request.POST['name']
		pprice = request.POST['price']
		pqty = request.POST['quantity']
		d1 = {
        	"p_no":pno,
        	"p_name":pname,
        	"p_price":pprice,
        	"p_quantity":pqty
       		 }
		json_data = json.dumps(d1)
		try:
			resp = requests.post("http://127.0.0.1:8000/addproduct/",json_data)
			if resp:
				return render(request,"addproduct.html",{"massage":"Product Saved SuccessFully","data":resp.json()})
			else:
				return render(request,"addproduct.html",{"massage":"Please Provide Valid Data"})
		except requests.exceptions.ConnectionError:
			return render(request,"addproduct.html",{"massage":"Server Not Available"})
	def put(self,request,*args,**kwargs):
		




	

















