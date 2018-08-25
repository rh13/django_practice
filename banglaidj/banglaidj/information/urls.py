from django.urls import path
from . import views

urlpatterns = [
	path('districts/', views.district_list, name='districts'),
	path('divisions/', views.division_list, name='divisions'),
	path('dists_of_div/<int:div_id>/',views.dists_of_div, name='dists_of_div'),
]