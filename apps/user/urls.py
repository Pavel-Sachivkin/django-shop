from xml.etree.ElementInclude import include
from django.urls import path,include
from .views import LoginView,LogoutView

app_name = 'user'
urlpatterns = [
    # path('', include('django.contrib.auth.urls'))
    # path('create/', UserCreateView.as_view(), name='create'),
    path('login/', LoginView.login_user, name='login'),
    path('logout/', LogoutView.logout_user, name='logout'),
]
