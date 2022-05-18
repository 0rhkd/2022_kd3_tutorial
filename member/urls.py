from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'member'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',
      auth_views.LoginView.as_view(
          template_name='member/login.html'
      ),   # Class Based View 클래스 기반의 뷰
      name='login'
),
path('logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
),

]