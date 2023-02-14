from django.db import models
from profiles.models import User

# Create your models here.

def upload_to(instance, image):
    return 'images/{image}'.format(image=image)

class Imagesubmissions(models.Model):
    uploader = models.ForeignKey(
        User, related_name="images", on_delete=models.CASCADE
    )
    image_file = models.ImageField(upload_to=upload_to, blank=True, null=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

