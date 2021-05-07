from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('bookmark/', views.bookmark, name="bookmark"),

    path('', views.latest, name="latest"),
    path('archive/', views.archive, name="archive")
]
