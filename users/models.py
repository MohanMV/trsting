from django.db import models
from django.contrib.auth.models import User
#import user models 
from PIL import Image


#creating a one to one relationship between a profile and a user, so one user can only have one profile and vice versa

#inherit from models.Model
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) #1to1 relationship with user
  #CASCADE = if user is deleted profile will be deleted too.but if profile is deleted, user won't be deleted.

  image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')

  #default = default.jpg is the default image users are handed
  #upload_to = profile_pics is the directory the profile pics are uploaded to

  def __str__(self):
    return f'{self.user.username} Profile'

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
      output_size = (300,300)
      img.thumbnail(output_size)
      img.save(self.image.path)