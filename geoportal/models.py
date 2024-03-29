from django.contrib.gis.db import models
from django.urls import reverse
from apps.users.models import User
from django.utils import timezone


class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name

class GetFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="geoportal/data/")

    def __str__(self):
        return self.title
    

class Post(models.Model):
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    place_name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return "{} + {}".format(self.owner, self.title)


    def approved_comments(self):
        return self.comments.filter(approved_comment=True)



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



class Tag(models.Model):
    title = models.CharField('title', max_length=100)

    def __str__(self):
        return "{}+++{}".format(self.title, self.posts)
