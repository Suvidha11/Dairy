from django.urls import path
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('add_post', views.add_post, name='add_post'),
   path('your_post', views.your_post, name='your_post'),
   path('delete/<int:id>', views.del_post, name='del_post'),
   path('Update/<int:id>/', views.Update_post, name='Update'),
   path('display/<int:id>', views.display, name='display'),
 
  ]