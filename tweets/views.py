from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.conf import settings
from .serializers import *
from .models import *
from .forms import *

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.
def home(request):
    return render(request, "pages/index.html", status=200)


def tweet_create(request, *args, **kwargs):
    user = request.user
    data = request.POST or None
    serializer = TweetSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user)

    return JsonResponse({}, status=201)















def tweet_list(request):

    data_set    = Tweets.objects.all()
    data_set_list =  [ x.serialize() for x in data_set ]
    context = {
        "response" : data_set_list
    }
    return JsonResponse(context)



def detail_view(request, pk):

    context = {'id':pk}
    status  = 200
    try:
        tweet = Tweets.objects.get(id=pk)
        context['content'] = tweet.content
    except:
        raise Http404
        context['messege'] = "Not found"
        status             = 404
   
    return JsonResponse(context,status)