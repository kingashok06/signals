from django.urls import path
from accounts.views import login_page,register_page
urlpatterns = [path('login' , login_page, name="1ogin"),path('register' , register_page, name="register")]