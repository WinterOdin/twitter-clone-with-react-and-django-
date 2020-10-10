from django import forms
from .models import *

MAX_LENGHT  = 256

class TweetForm(forms.ModelForm):
    class Meta:
        model   = Tweets
        fields  = ['content']  

    def clean_content(self):
        
        content = self.cleaned_data.get('content')
        if len(content) > MAX_LENGHT:
            raise forms.ValidationError("tweet is too long")
        return content