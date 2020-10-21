from django.contrib import admin
from .models import *



class TweetAdmin(admin.ModelAdmin):
    list_display  = ['__str__', 'user']
    search_fields = ['user__username', 'user__email']
    class Meta:
        model = Tweets



admin.site.register(Tweets, TweetAdmin)