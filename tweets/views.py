from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render



from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, "pages/index.html", status=200)

def tweet_create(request): 
    
    form = TweetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TweetForm()
    context = {
        "form" : form,
    }
    return render( request, 'components/forms.html', context)

def tweet_list(request):

    data_set    = Tweets.objects.all()
    data_set_list =  [{ "id": x.id, "content" : x.content, "likes":12} for x in data_set ]
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