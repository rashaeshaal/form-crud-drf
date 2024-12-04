from django.urls import path
from .views import StateListView, DistrictListView, PostView

urlpatterns = [
    path('states/', StateListView.as_view(), name='state-list'),
    path('districts/<int:state_id>/', DistrictListView.as_view(), name='district-list'),
    path('posts/', PostView.as_view(), name='post-list-create'),
    path('posts/<int:post_id>/', PostView.as_view(), name='post-edit-delete'),
    path('get/api', PostView.as_view(), name='get_posts'),
    path('posts/<int:post_id>/', PostView.as_view(), name='post-detail'),
    path('api/posts/<int:id>/', PostView.as_view(), name='post-detail'),
 
]
