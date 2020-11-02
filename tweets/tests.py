from django.test import TestCase
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.test import APIClient

# Create your tests here.
class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="abc", password="pass!@#")
        Tweets.objects.create(content="tweet 1", user=self.user)
        Tweets.objects.create(content="tweet 2", user=self.user)
        self.currentCount = Tweets.objects.all().count()

    def test_tweet_created(self):
        tweet_data = Tweets.objects.create(content="tweet 2", user=self.user)
        self.assertEqual(tweet_data.user, self.user)
    
    def get_client(self):
        test_user = APIClient()
        test_user.login(username=self.user.username, password='pass!@#')
        return test_user

    def test_tweet_detail(self):
        test_user = self.get_client()
        response  = test_user.get("tweets/detail/1/")
        self.assertEqual(response.status_code, 200)
        data      = response.json()
        tweet_id  = data.get("id")
        self.assertEqual(tweet_id, 1)
    
    def test_tweet_delete(self):
        test_user = self.get_client()
        response  = test_user.get("deleteTweet/1/delete/")
        self.assertEqual(response.status_code, 200)       
        test_user = self.get_client()
        response  = test_user.get("deleteTweet/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_is_incorrect = test_user.get("deleteTweet/2/delete/")
