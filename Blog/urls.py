from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('about/', views.About, name="About"),
    path('contact/', views.Contact, name="Contact"),
    path('dashboard/', views.Dashboard, name="Dashboard"),
    path('register/', views.Register, name="Register"),
    path('login/', views.Login, name="Login"),
    path('logout/', views.Logout, name="Logout"),
    path('addpost/', views.AddPost, name="AddPost"),
    path('updatepost/<int:id>', views.UpdatePost, name="UpdatePost"),
    path('deletepost/<int:id>', views.DeletePost, name="DeletePost"),
]
