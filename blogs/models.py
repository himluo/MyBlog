from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Tag(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model, HitCountMixin):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    user_id = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='photo')
    summary = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    blog_id = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)



