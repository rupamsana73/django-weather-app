from django.urls import path
from . import views

urlpatterns = [
    # AUTH
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # WEATHER PAGE
    path('weather/', views.weather_home, name='weather'),
    # WEATHER API
    path('api/weather/', views.get_weather, name='get_weather'),
    # FORECAST    
    path('api/forecast/', views.get_forecast, name='get_forecast'),
    # LOGOUT
     path('logout/', views.logout_view, name='logout'),
    # ABOUT
    path('about/', views.about_view, name='about'),

]

