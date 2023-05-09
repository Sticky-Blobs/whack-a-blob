from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import apis


app_name = 'users'

urlpatterns = [
    path('login', apis.LoginAPI.as_view(), name='login'),
    
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
