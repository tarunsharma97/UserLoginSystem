from django.contrib.auth.forms import AuthenticationForm
from django.utils import html
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.userlist, name='home'),

    path('registration/', views.Registration.as_view(),
         name='registration'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',
                                                         authentication_form=LoginForm), name='login'),
                                                

    path('edit/<int:id>/', views.edituser, name='edit'),
                                            
    path('delete/<int:id>/', views.deleteuser, name='delete'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]