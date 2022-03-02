from django.urls import path
from . import views
from .views import ModelListView
#from user import views

urlpatterns = [
    path('', views.Homepage, name='home'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name='signup'),
    path("dashboard", views.index, name="index"),
    path("Employee details", ModelListView.as_view(), name='employee_details'),
    #path("profile", views.profile, name="profile"),
    #path('profile', views.ProfileView.as_view(), name='profile')
    
]
