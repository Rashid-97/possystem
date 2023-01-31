from django.db import models
from django.contrib.auth.models import User as CoreUser


class User(CoreUser):
    profile_picture = models.ImageField(upload_to='images/user', null=True, default='images/user/profilepictures.png')
    is_manager = models.BooleanField(default=False)
    belongs_to = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)
