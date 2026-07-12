from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/',register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('update-profile/', update_profile, name='update_profile'),
    path('change-password/', change_password, name='change_password'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset-password/', reset_password, name='reset_password'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]