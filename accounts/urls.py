from django.urls import path

from . import views

urlpatterns = [
    path('login',views.login_user,name='login'),
    path('registration',views.registration,name='registration'),
    path('logout',views.logout,name='logout')
]
