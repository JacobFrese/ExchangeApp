"""TEX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from core import views as core_views
from toolExchange import views as toolExchange_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home),
    path('join/', core_views.user_join),
    path('login/', core_views.user_login),
    path('logout/', core_views.user_logout),
    path('about/', core_views.about),
    path('profile/', core_views.profile),
    path('profile/edit/<int:id>/', core_views.edit),
    path('toolExchange/', toolExchange_views.toolExchange),
    path('toolExchange/post/', toolExchange_views.post),
    path('toolExchange/search_tool/', toolExchange_views.search_tool),
    path('toolExchange/search_category_button/', toolExchange_views.search_category_button),
    path('toolExchange/toggle/<int:id>/', toolExchange_views.toggle),
    path('toolExchange/request/<int:id>/', toolExchange_views.request),
    path('toolExchange/edit/<int:id>/', toolExchange_views.edit),
]
