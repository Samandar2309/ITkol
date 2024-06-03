from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Single_offers(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    svg = models.FileField(upload_to='images/')

    def __str__(self):
        return self.name


class Category_name(TimeStampedModel):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=50)
    icon = models.FileField(upload_to='images/')

    def __str__(self):
        return self.name


class Information(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Numbers(TimeStampedModel):
    description = models.TextField()

    def __str__(self):
        return self.description


class Blog(TimeStampedModel):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Case(TimeStampedModel):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')
    information = models.CharField(max_length=212)
    company = models.CharField(max_length=212)
    icon = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Contact(TimeStampedModel):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Video(TimeStampedModel):
    url = models.URLField()
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
