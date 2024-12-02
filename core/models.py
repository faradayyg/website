from django.db import models

# from django.contrib.postgres.fields import ArrayField
from taggit.managers import TaggableManager

# Create your models here.


class PostTagChoices(models.TextChoices):
    MUSIC = "music", "Music"
    NICHE = "niche", "Niche"
    NEW_INTEREST = "new_interest", "New Interest"
    DAY_IN_LIFE = "day_in_life", "Day In Life"
    ART = "art", "Art"
    SOMETHING_COOL = "something_cool", "Something Cool"


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "-").lower()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
