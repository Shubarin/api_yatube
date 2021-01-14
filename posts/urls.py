from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet, UserViewSet


router = DefaultRouter()
router.register('api/v1/users', UserViewSet, basename='UserView')
router.register(r'api/v1/posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                basename='CommentView')
router.register('api/v1/posts', PostViewSet, basename='PostView')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
