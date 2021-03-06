from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    image=models.ImageField(upload_to='post_pics')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
   
  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

   



class Comment(models.Model):
    Select_Question = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    Your_name=models.CharField(max_length=250)
    Reply=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.Question)+str(self.Your_name)


