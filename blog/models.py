from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse


class PublisedManager(models.Manager):
    def get_queryset(self):
        return super(PublisedManager,self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),related_name='posts',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS_CHOICES,max_length=10,default='draft')

    objects = models.Manager()
    published = PublisedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f"{self.title} by {self.author} "

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])