
from .models import *
from rest_framework import serializers
from django.conf import settings

MAX_LENGHT = settings.MAX_LENGHT
TWEET_ACTION = settings.TWEET_ACTION


class TweetLikeSerializer(serializers.Serializer):
    tweet_id    = serializers.IntegerField()
    action      = serializers.CharField()
    content     = serializers.CharField(allow_blank=True, required=False)
    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION:
            raise serializers.ValidationError("action is not valid")
        else:
            return value


class TweetCreateSerializer(serializers.ModelSerializer):
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


class TweetSerializer(serializers.ModelSerializer):
    likes   = serializers.SerializerMethodField(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)

    class Meta:
        model = Tweets
        fields = ['id','content','likes','is_retweet','parent']

    def get_likes(self,data):
        return data.likes.count()

    def get_content(self,value):
        content = value.content
        if value.is_retweet:
            content = value.parent.content
        return content