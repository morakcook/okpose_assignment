from django.urls import path, re_path
from .views import schema_view

urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
