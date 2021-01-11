from django.db import models
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('blog:home')
    
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture =  models.ImageField(null=True, blank=True, upload_to='profile_pictures/')
    facebook_url =  models.CharField(max_length=250)
    twitter_url = models.CharField(max_length=250)
    instagram_url = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('blog:home')
    
    def __str__(self):
        return self.user.username

    
class Post(models.Model):
    title = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    published = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=150, default='Coding')
    likes = models.ManyToManyField(User, related_name='blog_post')
    snippet = models.CharField(max_length=250, default='Click link')

    def get_total_like(self):
        return self.likes.count()




    def __str__(self):
        return  self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog:home')
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-date_added ']

    
    def __str__(self):
        return '%s - %s' %(self.post.title , self.name)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body =body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-date_added ']

    def __str__(self):
        return '%s - %s' %(self.comment.post.title , self.body)


