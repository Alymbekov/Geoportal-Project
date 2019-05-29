from django.contrib.gis.db import models
from django.urls import reverse
from apps.users.models import User
from django.utils import timezone

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
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

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


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


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(comment):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



class Tag(models.Model):
    title = models.CharField('title', max_length=100)

    def __str__(self):
        return "{}+++{}".format(self.title, self.posts)
