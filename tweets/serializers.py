
from .models import *
from rest_framework import serializers
from django.conf import settings

MAX_LENGHT = settings.MAX_LENGHT
TWEET_ACTION = settings.TWEET_ACTION


class TweetLikeSerializer(serializers.Serializer):
    tweet_id    = serializers.IntegerField()
    action      = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION:
            raise serializers.ValidationError("action is not valid")
        else:
            return value


class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweets
        fields = ['id','content','likes']

    def get_likes(self,data):
        return data.likes.count()

    def validate_content(self,value):
        if len(value) > MAX_LENGHT:
            raise serializers.ValidationError("tweet is too long")
        return value