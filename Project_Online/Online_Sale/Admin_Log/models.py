from django.db import models

# Create your models here.
class MarchantModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

class Admin_log(models.Model):
	admin_name = models.CharField(max_length=50)
	admin_password = models.CharField(max_length=10)

class Product_Model(models.Model):
	p_no = models.IntegerField(primary_key=True)
	p_name = models.CharField(max_length=50,unique=True)
	p_price = models.FloatField()
	p_quantity = models.IntegerField()
	#m_id = models.ForeignKey(MarchantModel,on_delete = models.CASCADE)