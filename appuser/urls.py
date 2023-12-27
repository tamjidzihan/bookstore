from django.urls import path
from . import views

app_name = 'appuser'

urlpatterns = [
    path('register',views.register,name="register"),
    path('log-in',views.log_in,name="log-in"),
    path('registration-error',views.registration_error,name='registration-error'),
    
    # test Urls
    path('user-info',views.user_info,name="user-info")
]