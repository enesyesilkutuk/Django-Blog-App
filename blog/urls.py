from django.urls import path
from .views import post_new, post_list, post_detail, PostDeleteView, PostUpdateView

urlpatterns = [
    path('post-new/', post_new, name='post_new'),
    path('post-list/', post_list, name='post_list'),
    path('post-detail/<str:slug>/', post_detail, name='post_detail'),
    path('post-delete/<str:slug>/', PostDeleteView.as_view(), name='post_delete'),
    path('post-update/<str:slug>/', PostUpdateView.as_view(), name='post_update'),
]