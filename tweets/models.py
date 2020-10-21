from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class Tweets(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=1)
    content = models.TextField(blank=True, null=True)
    image   = models.FileField(upload_to='images/', blank=True)
    class Meta:
        ordering = ['-id']
        
    def serialize(self):
        return{
            'id'        : self.id,
            'content'   : self.content,
            'likes'     : 0
        }

