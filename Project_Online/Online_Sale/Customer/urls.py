from django.urls import path
from Customer import views
urlpatterns = [
    path('cust/',views.ShowIndex,name="main"),
    path('register/',views.ShowRegister,name="Register"),
    path('saveregister/',views.SaveUser,name="SaveRegister"),
    path('login/',views.LoginPage,name="Login"),
    path('loginuser',views.LoginInto,name="LoginUser")
    
]