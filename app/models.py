from django.db import models
from django.core.exceptions import ValidationError

import os


# Create your models here.
def avatar_upload_path(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Generate a unique filename based on the nickname
    unique_filename = f"{instance.nickname}.{ext}"
    # Return the full path to save the image
    return os.path.join('app/media/avatar/', unique_filename)


class Client(models.Model):
    fullname = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255, null=True, unique=True)
    title = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    # save image to app/media/ folder with nickname as name
    avatar = models.ImageField(upload_to=avatar_upload_path, null=True, blank=True)
    avatar_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nickname


def validate_svg(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    if ext.lower() != '.svg':
        raise ValidationError('Only SVG files are allowed.')


class Button(models.Model):
    link = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=255, null=True)
    sub_text = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    logo = models.FileField(upload_to='app/media/logo/', null=True, blank=True, validators=[validate_svg])
    logo_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.text
