from django.urls import path
from . import views
urlpatterns = [
	path('', views.home),
    path("tweets/<str:tweet_id>/", views.detail_view, name="tweets"),
    path("tweetList", views.tweet_list, name="tw"),
    path('createTweet', views.tweet_create, name='createTweet'),
    path('deleteTweet/<str:tweet_id>/delete', views.delete_view, name='deleteTweet')

]