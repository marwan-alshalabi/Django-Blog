from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.
# ORM : Operational Relational Maper
'''
    table
        column : name : str : options (100 char)
        column : age : int : options (+12)

    ORM (class)---> sql :db
    
    class : name
        field : name : str : options
'''

'''
ORM : 
    - html widget
    - validation
    - handl db
'''

class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post')
    tags = TaggableManager()
    
    def __str__(self):
        return self.name
