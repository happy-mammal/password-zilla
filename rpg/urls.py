from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='rpg-home'),
    path('about/', views.about, name='rpg-about'),
    path('generator/', views.generator, name='rpg-generator'),
    path('tips/', views.tips, name='rpg-tips'),
    path('signup/', views.signup, name='rpg-signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='rpg/signin.html'),name='rpg-signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='rpg/signout.html'),name='rpg-signout'),
   
]
