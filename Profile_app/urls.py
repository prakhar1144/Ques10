from django.urls import path
from .views import profile,user_edit,home,signUp


urlpatterns = [
    path('', home, name="home"),
    path('profile/', profile, name="profile"),
    path('user/<int:pk>/edit/', user_edit, name='user_edit'),
    path('signup/', signUp, name='signup'),
]


