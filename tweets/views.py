from django.shortcuts import render
from .models import Tweets
from django.http import HttpResponse, Http404, JsonResponse



# Create your views here.
def home(request):

    return render(request, "pages/index.html", status=200)


def tweet_list(request):

    data_set    = Tweets.objects.all()
    data_set_list =  [{ "id": x.id, "content" : x.content} for x in data_set ]
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