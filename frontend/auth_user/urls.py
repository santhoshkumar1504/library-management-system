from django.urls import path
from .views import *

urlpatterns = [

    path('register/', register, name='register'),

    path('', login, name='login'),

    path('logout/', logout, name='logout'),

    path('profile/', profile, name='profile'),

    path('update-profile/', update, name='update'),

    path('change-password/',change_password, name='change_password'),

    path('forgot-password/', forgot_password, name='forgot_password'),

    path('reset-password/', reset_password, name='reset_password'),

]