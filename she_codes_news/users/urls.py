from django.urls import path 
from .views import CreateAccountView, UserListView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('create/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/', UserListView.as_view(), name = 'list'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name = 'profile'),
    path('profile/<str:slug>/',UserProfileView.as_view(), name = 'profile'),
]