"""article URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.urls import path

from blogapp.views import ArticleDetailView, ArticleListView
from blogapp.views import CreateArticle
from blogapp.views import SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', ArticleListView.as_view(), name='home'),
    path('create/', CreateArticle.as_view(), name='create'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(template_name='blogapp/html/login.html'), name='login'),
    path('home/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path("logout/", LogoutView.as_view(template_name='blogapp/html/logout.html', next_page='home'), name="logout"),
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
