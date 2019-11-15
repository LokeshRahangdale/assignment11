from django.shortcuts import render
from .models import *
# Create your views here.
def ShowIndex(request):
	return render(request,"Admin/index.html")

def login_user(request):
	if request.method=="POST":
		username = request.POST['uname']
		password = request.POST['pass']
		user = Admin_log.objects.get(admin_name=username,admin_password=password)
		if request.method=="POST":
			if user:
				return render(request,"Admin/usercheck.html",{"massage":"Welcome Admin"})
			else:
				return render(request,"Admin/index.html",{"massage":"Invalid Credentials"})
		else:
			return render(request,"Admin/index.html")
	else:
		return render(request,"Admin/index.html")


def Add_Marchant(request):
	qs=MarchantModel.objects.all()
	return render(request,"Admin/addmarchant.html",{"data":qs})

def SaveMarchant(request):
	if request.method=="POST":
		name = request.POST['name']
		contact = request.POST['contact']
		email = request.POST['email']
		res = MarchantModel.objects.all()
		if request.method == "POST":
			if res:
				for x in res:
					idno = int(x.idno)
			else:
				idno = 100
			while True:
				idno = idno+1
				try:
					pid = idno
					plen=len(name)
					padd=str(pid+plen)
					pcont=list(contact)
					pemail = list(email)
					password =str(pemail[0]+pcont[-1]+padd[:2]+pemail[1]+padd[-1]+pcont[0]+pemail[2])
					MarchantModel(idno=idno,name=name,contact=contact,email=email,password=password).save()
				except ValueError:
					return render(request,"Admin/addmarchant.html",{"massage":"Please Provide Valid Data Only"})
				else:
					qs=MarchantModel.objects.all()
					return render(request,"Admin/addmarchant.html",{"data":qs})
		else:
			return render(request,"Admin/addmarchant.html",{"data":qs})
	else:
		return render(request,"Admin/addmarchant.html",{"data":qs})

def DeleteMarchant(request):
	mid = request.GET['id']
	MarchantModel.objects.filter(idno=mid).delete()
	qs = MarchantModel.objects.all()
	return render(request,"Admin/addmarchant.html",{"data":qs})



from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
from django.http import HttpResponse
from .forms import MarchantForm , ProductForm
@method_decorator(csrf_exempt,name="dispatch")
class Marchant_Login_Check(View):
	def post(self,request):
		data = request.body
		d1 = json.loads(data)
		uname = d1['uname']
		upass = d1['upass']
		try:
			res = MarchantModel.objects.get(email=uname,password=upass)
			if res:
				return HttpResponse(res)
		except:
			return HttpResponse(res)

@method_decorator(csrf_exempt,name="dispatch")
class AddProduct(View):
	def post(self,request):
		data = request.body
		d1 = json.loads(data)
		p_no = d1['p_no']
		p_name = d1['p_name']
		p_price = d1['p_price']
		p_quantity = d1['p_quantity']
		try:
			Product_Model(p_no=p_no,p_name=p_name,p_price=p_price,p_quantity=p_quantity).save()
		except:
			return HttpResponse(content_type="application/json")
		finally:
			product_data = Product_Model.objects.all()
			json_data = serialize("json",product_data,fields=('p_no','p_name','p_price','p_quantity'))
			return HttpResponse(json_data,content_type="application/json_data")

		# pf = ProductForm(d1)
		# res = pf.save(commit=True)
		# return HttpResponse(res)

	# def get(self,request):
	# 	qs =Product_Model.objects.all()
	# 	json_data = serialize("json",qs)
	# 	return HttpResponse(json_data,content_type="application/json")





























