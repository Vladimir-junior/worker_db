from django.contrib import admin
from django.urls import path

from users.views import search_employee, index

urlpatterns = [
    path('', index,name="index"),
    path('admin/', admin.site.urls, name='admin_panel'),
    path('search/', search_employee, name='search_employee'),
]
