from django.urls import path
from .views import UserRegistrationAPIView, LoginAPIView, UserProfileAPIView, UserProfileListAPIView, UserProfileDetailView

urlpatterns = [
    path('api/register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/profile/', UserProfileAPIView.as_view(), name='user-profile'),
    path('api/profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    path('api/profiles/', UserProfileListAPIView.as_view(), name='user-profiles'),
]