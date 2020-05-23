from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='https://www.pngitem.com/pimgs/m/192-1926160_transparent-ajax-png-anime-profile-png-download.png', upload_to='profile_pics')
    description = models.CharField(max_length = 5000, default='enter description')
    li = models.CharField(max_length = 2000, default = 'home')
    insta = models.CharField(max_length = 2000, default = 'instagram')
    def __str__(self):
        return f'{self.user.username} Profile'

class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to= 'book')
    cover = models.ImageField(upload_to='covers', null=True,blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args,**kwargs)

class Topic(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Book, on_delete=models.CASCADE,)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic ,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Query(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text