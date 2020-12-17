from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_new, name='enter_new_text'),
    path('/<int:pk>/', views.post_detail, name='post_detail'),
]
