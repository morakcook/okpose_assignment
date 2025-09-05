from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


"""
DefaultRouter 모듈을 통해 기본적인 CRUD URL 을 생성합니다.
추가적으로
tags, product_options URL은 데이터 확인용입니다.
"""


# Router 선언
router = DefaultRouter()

# Router에 View 등록 (CRUD URL 자동 생성)
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"tags", views.TagView, basename="tag")
router.register(r"product_options", views.ProductOptionView, basename="product_option")

# 최종 URL 패턴 등록
urlpatterns = [
    path("", include(router.urls)),
]
