from cgitb import lookup
from http import client
from django.contrib import admin
from django.db import router
from django.urls import path, include
from Topic.views import TopicModelViewSet, UserModelViewSet
from post.views import PostModelViewSet
from comment.views import CommentModelViewSet
from rest_framework.routers import DefaultRouter
from  rest_framework_nested import routers

router = DefaultRouter()

router.register('topic', TopicModelViewSet, basename = 'topic')
# router.register('user', UserModelViewSet, basename = 'user')
# router.register('post', PostModelViewSet, basename = 'post')

post_router = routers.NestedSimpleRouter(router, 'topic', lookup = 'topic')
post_router.register('post', PostModelViewSet, basename = 'post')

comment_router = routers.NestedDefaultRouter(post_router, 'post', lookup = 'post')
comment_router.register('comment', CommentModelViewSet, basename = 'comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(post_router.urls)),
    path('', include(comment_router.urls)),
    path("api-auth/", include("rest_framework.urls")),  
]
