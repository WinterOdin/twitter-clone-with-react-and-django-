
from .models import *
from rest_framework import serializers
from django.conf import settings


MAX_LENGHT = settings.MAX_LENGHT

class TweetLikeSerializer(serializers.Serializer):
    id     = serializers.IntegerField()
    action = serializers.CharField()


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['content']

    def validate_content(self,value):
        if len(value) > MAX_LENGHT:
            raise serializers.ValidationError("tweet is too long")
        return value