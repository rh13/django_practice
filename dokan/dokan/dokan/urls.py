from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('inventory/', include('inventory.urls'), name='inventory'),

]
