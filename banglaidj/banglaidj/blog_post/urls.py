from django.urls import path
from . import views

urlpatterns = [
    path('post-list/', views.post_list, name='post-list'),
    path('single-post/<post_id>/', views.single_post, name='single-post')
]
