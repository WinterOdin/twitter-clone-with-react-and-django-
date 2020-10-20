from django.db import models

# Create your models here.
class Tweets(models.Model):

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

