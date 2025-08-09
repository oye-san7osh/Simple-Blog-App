from django.db import models
from django.utils import timezone
from django.utils.text import slugify



# Create your models here.
class Post(models.Model):
    post_name = models.CharField(max_length = 100)
    post_detail = models.TextField(max_length = 1000)
    created_by = models.CharField(max_length = 100)
    post_time = models.TimeField(default = timezone.now)
    post_date = models.DateField(default = timezone.now)
    slug_link = models.SlugField(null = True, blank = True, unique = True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug_link:
            self.slug_link = slugify(self.post_name)
        super().save(*args, **kwargs)