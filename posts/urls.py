from django.conf.urls import url
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from yatube_api.settings import description_swagger

from .views import CommentViewSet, PostViewSet, UserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='Yatube API',
        default_version='v1',
        description=description_swagger,
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='kirill.shubarin@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]

router = DefaultRouter()
router.register('api/v1/users', UserViewSet, basename='UserView')
router.register(r'api/v1/posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                basename='CommentView')
router.register('api/v1/posts', PostViewSet, basename='PostView')

urlpatterns += [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
