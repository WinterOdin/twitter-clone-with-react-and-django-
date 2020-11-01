from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweets", on_delete=models.CASCADE)
    time  = models.DateTimeField(auto_now_add=True)

# Create your models here.
class Tweets(models.Model):
    parent  = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    likes   = models.ManyToManyField(User, related_name="tweet_user", blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image   = models.FileField(upload_to='images/', blank=True)
    time    = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-id']
        
    def serialize(self):
        return{
            'id'        : self.id,
            'content'   : self.content,
            'likes'     : 0
        }

