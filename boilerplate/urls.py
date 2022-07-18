from django.urls import path, include
from . import views 

urlpatterns = [
        path('login/', views.login_page, name='login_page'),
        path('profile/', views.profile_show, name='profile'),
        path('logout/', views.logout_view, name='logout'),
        path('signup/', views.register, name='signup_form'),
]