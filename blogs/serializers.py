from rest_framework import serializers
from .models import Blog, Comment, Tag
from hitcount.models import HitCount


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'id', 'name')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
    hits = serializers.ReadOnlyField(source='hit_count_generic.first.hits')
    tags = TagSerializer(many=True)

    class Meta:
        model = Blog
        fields = ('url', 'id', 'name', 'image', 'summary', 'content', 'created_at', 'comments', 'hits', 'tags')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'id', 'content', 'created_at')



