from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

class Post(models.Model):
    
    STATUS = (
        (0, "Draft"),
        (1, "Publish"),
    )

    CATEGORY = (
        ("FE","Frontend"),
        ("BE","Backend"),
        ("FS","Fullstack"),
    )

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now= True)
    category = models.CharField(choices=CATEGORY, default="FS", blank=True, max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)

    # class Meta:
    #     ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)+str(uuid.uuid4())
        return super().save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content