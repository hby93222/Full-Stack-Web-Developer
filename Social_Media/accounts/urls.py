from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# auth_views provides new features: loginview and logoutview


app_name = 'accounts'

urlspatterns = [

 path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
 path('logout/',auth_views.LogoutView.as_view(),name='logout'),
 path('signup/',views.SignUp.as_view(),name='signup')
]
