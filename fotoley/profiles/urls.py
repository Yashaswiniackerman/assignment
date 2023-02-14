from rest_framework.authtoken import views
from django.urls import path
from profiles.views import registration_view


urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('signup/', registration_view)
]