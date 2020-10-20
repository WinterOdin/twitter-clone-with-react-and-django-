from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.conf import settings

from .models import *
from .forms import *

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.
def home(request):
    return render(request, "pages/index.html", status=200)

def tweet_create(request): 
    form = TweetForm(request.POST or None)
    url  = request.POST.get('next') or None

    if form.is_valid():

        data = form.save(commit=False)
        form.save()

        if request.is_ajax():
           return JsonResponse(data.serialize(), status=201)
        if url != None and is_safe_url(url, ALLOWED_HOSTS):
            return redirect(url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors,status=400)
    context = {
        "form" : form,
    }
    return render( request, 'components/forms.html', context)

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