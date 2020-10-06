from django.urls import path
from . import views
urlpatterns = [
	path('', views.home),
    path("tweets/<str:pk>/", views.detail_view, name="tweets"),
    path("tweetList", views.tweet_list, name="tw")

]