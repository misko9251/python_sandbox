from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name='profile'),
    # login and logout below come from line 2. these are class based views. the built in views for login and logout handle both the forms and logic (not the templates, we must create those) We must tell django where to look for the template, hence template_name
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', user_views.logout_view, name='logout'),
    path('renoreddit/', include('renoreddit.urls')),
]
