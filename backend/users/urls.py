from django.urls import path
from .api.views import ToggleFavoriteView, UserRegistrationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('favorites/toggle/<int:property_id>/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
    
]