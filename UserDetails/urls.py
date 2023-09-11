from django.urls import path
from .views import user_management  # Import views from the absolute path

urlpatterns = [
    # URLs for User_details model
    path('users/<int:pk>/',  user_management, name='user-detail'),
    path('users/',  user_management, name='user-list'),

    # URLs for User_Address model
    path('addresses/<int:pk>/', user_management, name='user-address-detail'),
    path('addresses/', user_management, name='user-address-list'),
]
