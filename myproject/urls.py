"""
프로젝트의 기본 URL 파일입니다.
여기서 필요한 작업의 APP 을 통하기 위해 해당 APP의 URL로 통하는 분기 처리를 진행합니다.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('doc/', include('doc.urls')),
]
