from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('register',views.register, name="register"),
    path('addFavorite',views.addToFavorite, name="home"),
    path('deleteFavorite',views.deleteFromFavorite, name="home"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('',views.home,name="home")
]
