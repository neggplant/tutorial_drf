from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('snippets.urls')),
]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [url(r'^swagger(?P<format>\.json|\.yaml)$',
                    schema_view.without_ui(cache_timeout=0),
                    name='schema-json'),
                url(r'^swagger/$',
                    schema_view.with_ui('swagger',
                                        cache_timeout=0),
                    name='schema-swagger-ui'),
                url(r'^redoc/$',
                    schema_view.with_ui('redoc',
                                        cache_timeout=0),
                    name='schema-redoc'),
                ]
