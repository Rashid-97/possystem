from django.db import models
from django.contrib.auth.models import User as CoreUser


class User(CoreUser):
    profile_picture = models.ImageField(upload_to='images/user')
