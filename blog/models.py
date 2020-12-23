from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    # Django DateTimeFields
    # the current date and time is assigned whenever an instance of the class is created
    created_on = models.DateTimeField(auto_now_add=True)
    # the current date and time is assigned whenever an instance of the class is saved i.e. when edited
    last_modified = models.DateTimeField(auto_now=True)

    # links our models for categories and posts in a such a way that many categories can be assgned to many posts
    categories = models.ManyToManyField('Category', related_name="posts")

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    # unlike ManyToManyField, ForeignKey relates `Post` and `Comment` in one way
    post = models.ForeignKey("Post", on_delete=models.CASCADE)