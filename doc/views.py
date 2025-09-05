from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="오케이포스 백엔드 코딩테스트",
        default_version='',
        description="상품 CRUD기능 API 문서"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
