from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here. 
# Making a class(table) for a post
# each class is gonna be its own table in the database



class Post(models.Model):
  #creating attributes, each attribute will be a different field in the database
  #so basically what each post should have
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now)
  #creating a foreign key and putting the user because its the related table. a one to many relationship. One user can have many posts but one post can only have one user. 
  #The on_delete is for when the user is deleted what happens to the posts in this case models.CASCADE tells it to delete the posts as well
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk':self.pk})

