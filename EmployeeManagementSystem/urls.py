"""EmployeeManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from employee import views as employee_views
from employee import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ems/login/', employee_views.LoginView.as_view(), name='login'),
    path('ems/logout/', employee_views.logout_view, name='logout'),

    path('', employee_views.index, name='index_page'),
    path('ems/employee/', employee_views.EmployeeView.as_view(), name='employee_view'),
    path('ems/employee/register/', employee_views.EmployeeRegister.as_view(), name='employee_register'),

    #API CALLS
    path('api/get_provinces/', api.get_provinces),
    re_path(r'^api/get_citymuni/(?P<province>[\w\s]*)$', api.get_citymuni),
]
