from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 130)
    img = models.ImageField(upload_to = 'pics')
    timestamp = models.DateTimeField(blank = True)
    # field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) 
 
 
    def __str__(self):
        return 'Message from ' + self.title + 'by' + self.author




    