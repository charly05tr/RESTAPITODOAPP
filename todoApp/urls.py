from rest_framework import routers
from .api import *
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/tasks', TaskViewSet, 'tasks')
router.register('api/users', UserViewSet, 'users')
urlpatterns = [path('', include(router.urls)), 
               path('api/register',RegisterView.as_view(), name='register'),
               path('api/change-password', ChangePasswordView.as_view(), name='change-password'),
               path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
               path('api/reset-password/', ResetPasswordRequestView.as_view(), name='reset_password_request'),
               path('api/reset-password-confirm/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm')]