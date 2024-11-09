from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255, blank=True, null=True)
    born_location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Quote(models.Model):
    tags = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()

class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    is_sent = models.BooleanField(default=False)
