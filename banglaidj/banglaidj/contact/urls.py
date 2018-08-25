from django.urls import path
from . import views

urlpatterns = [
	path('clist/', views.my_contact, name='contact-list'),
	path('cadd/', views.add_contact, name='add_contact'),
	path('edit/<int:contact_id>/', views.edit_contact, name='edit-contact'),
	path('delete/<int:contact_id>/', views.delete_contact, name='delete-contact')
	
]
