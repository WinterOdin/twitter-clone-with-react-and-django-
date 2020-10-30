import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from .forms import *

ALLOWED_HOSTS = settings.ALLOWED_HOSTS



def home(request):
    return render(request, "pages/index.html", status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_create(request, *args, **kwargs):
    user = request.user
    serializer = TweetSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        data_chunk = serializer.save(user= user)
        return Response(serializer.data, status=201)
    return Response({},status=400)





@api_view(['GET'])
def tweet_list(request):
    data_set    = Tweets.objects.all()
    serializer  = TweetSerializer(data_set, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def detail_view(request, tweet_id):
    data_set    = Tweets.objects.filter(id=tweet_id)
    if not data_set.exists():
        return Response({}, status=404)
    data_set    = data_set.first()
    serializer  = TweetSerializer(data_set)
    return Response(serializer.data, status=200)



@api_view(["DELETE", "POST"])
@permission_classes([IsAuthenticated])
def delete_view(request, tweet_id):
    data_set = Tweets.objects.filter(id=tweet_id)
    if not data_set.exists():
        return Response({}, status=404)
    data_set = data_set.filter(user=request.user)
    if not data_set.exists():
        return Response({"message": "error"}, status=401)
    data = data_set.first()
    data.delete()
    return Response({"message": "Tweet removed"}, status=200)

@api_view(["DELETE", "POST"])
def like_view(request, tweet_id):
    serializer = TweetLikeSerializer(request.POST)
    if serializer.is_valid(raise_exception=True):
        data     = serializer.validated_data
        tweet_id = data.get("id")
        action   = data.get("action")

        data_set   = Tweets.objects.filter(id=tweet_id)
        if not data_set.exists():
            return Response({}, status=404)
        data = data_set.first()
        if action == "like":
            data.likes.add(request.user)
        elif  action == "unlike":
            data.likes.remove(request.user)
        elif action: # 4 08
            pass
   
    return Response({"message": "Tweet removed"}, status=200)