from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('Signup/',views.SignUp_view,name="SignUp"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout")
]
