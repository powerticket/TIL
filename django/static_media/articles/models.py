from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90}
    )
