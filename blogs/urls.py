from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'tags', views.TagViewSet)


urlpatterns = [
    url(r'^$', views.blogs, name='blogs'),
    url(r'^blog/(?P<id>[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})/$', views.blog, name='blog'),
    url(r'^tag/(?P<id>[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})/$', views.blogs_tag, name='blogs_tag'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]