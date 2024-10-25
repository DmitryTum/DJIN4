from django.urls import path

from .views import PostList, post_share, post_detail, post_comment, post_list
from .views import post_search
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    # path('', PostList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:pk>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),

    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', post_search, name='post_search'),
]