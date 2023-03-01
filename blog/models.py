from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

alpha_only = RegexValidator(
    r'^[a-zA-Z\W]*$', 'Only alphabets and special characters are allowed.')


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, validators=[alpha_only])
    text = models.TextField(validators=[alpha_only])
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title
