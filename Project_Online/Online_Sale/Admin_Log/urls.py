from django.urls import path
from Admin_Log import views
urlpatterns = [
    path('index/',views.ShowIndex,name="index"),
    path('login_user/',views.login_user,name="Login"),
    path('add_marchant/',views.Add_Marchant,name="add_marchant"),
    path('savemarchant/',views.SaveMarchant,name="savemarchant"),
    path('deletemarchant/',views.DeleteMarchant,name="deletemarchant"),
    path('marchant_login/',views.Marchant_Login_Check.as_view()),
    path('addproduct/',views.AddProduct.as_view()),
]