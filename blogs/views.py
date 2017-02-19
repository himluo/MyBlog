from django.shortcuts import render
from .models import Blog, Comment, Tag
from rest_framework import viewsets
from .serializers import BlogSerializer, CommentSerializer, TagSerializer
from rest_framework import permissions
import hitcount
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blogs(request):
    blogs_list = Blog.objects.all()
    paginator = Paginator(blogs_list, 5)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        page = 1
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    page_view = 2
    pages_list = [x for x in range(int(page)-page_view, int(page)+page_view+1) if x >= 1 and x <= paginator.num_pages]
    if pages_list[0] != 1:
        pages_list.insert(0, 1)

    if pages_list[1] >= 3:
        pages_list.insert(1, '...')

    if pages_list[-1] != paginator.num_pages:
        pages_list.append(paginator.num_pages)

    if pages_list[-2] < paginator.num_pages - 1:
        pages_list.insert(-1, '...')

    return render(request, 'blogs/blogs.html', {
        'blogs': blogs,
        'pages': pages_list
    })


def blog(request, id):
    blog = Blog.objects.get(pk=id)
    hit_count = HitCount.objects.get_for_object(blog)
    hitcount.views.HitCountMixin.hit_count(request, hit_count)

    return render(request, 'blogs/blog.html', {
        'blog': blog,
        'next': Blog.objects.filter(created_at__gt=blog.created_at).last(),
        'prev': Blog.objects.filter(created_at__lt=blog.created_at).first(),
    })


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)