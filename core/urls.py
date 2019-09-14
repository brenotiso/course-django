from django.urls import (
    path,
    include
)
from django.contrib.auth import views as auth_views
from .views import (
    index,
    SignUp
)

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup')
]
