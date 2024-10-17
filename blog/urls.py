from django.urls import path

from .views import PostList, post_share, post_detail, post_comment

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:pk>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
]