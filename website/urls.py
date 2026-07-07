from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
