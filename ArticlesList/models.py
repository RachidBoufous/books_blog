from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Articles(models.Model):
    Title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50,blank=True)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    Logo = models.ImageField(default='def.png',blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    def fifthteenC(self):
        return self.body[:50] + '[...]'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Articles, self).save(*args, **kwargs)

