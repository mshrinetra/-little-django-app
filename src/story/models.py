from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Story(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    story_img = models.ImageField(
        default='default_story_iimg.jpg', upload_to='story_pic')
    content = models.TextField(max_length=500)
    pub_date = models.DateTimeField('Date Published', auto_now=True)

    def __str__(self):
        return self.title
