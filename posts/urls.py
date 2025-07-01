from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # URLS para las vistas de la API
    path('api/', views.PostListAPIView.as_view(), name='post_list_api'),
    path('api/<int:pk>/', views.PostDetailAPIView.as_view(), name='post_detail_api'),
]
