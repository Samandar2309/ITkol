from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ResenPost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class InstagramPost(models.Model):
    image = models.ImageField(upload_to='blogs')




class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Blog_detail(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs')
    description = models.TextField()
    second_description = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name
