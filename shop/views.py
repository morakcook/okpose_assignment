from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product, Tag, ProductOption
from .serializers import (
    ProductSerializer,
    TagSerializer,
    ProductOptionSerializer,
)


"""
메인적으로 
ProductViewSet 클래스를 통해서 데이터의 CRUD기능을 진행합니다.
추가적으로
데이터의 입력 확인을 위해
TagView,ProductOptionView 를 ReadOnlyModelViewSet 모듈을 사용하여 읽기 작업만 진행합니다.
"""


class ProductViewSet(viewsets.ModelViewSet):
    """상품 CRUD 뷰셋"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TagView(viewsets.ReadOnlyModelViewSet):
    """태그 조회 전용 뷰셋"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductOptionView(viewsets.ReadOnlyModelViewSet):
    """상품 옵션 조회 전용 뷰셋"""

    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
