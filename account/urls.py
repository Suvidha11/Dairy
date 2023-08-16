from django.urls import path
from . import views
urlpatterns = [   
   path('user_login', views.user_login, name='user_login'),
   path('', views.signup, name='signup'),
   path('user_logout', views.user_logout, name='user_logout'),
   path('otp', views.otp_verify, name='otp'),  
]