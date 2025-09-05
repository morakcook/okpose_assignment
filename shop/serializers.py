# 직렬화/역직렬화 작업
# 직렬화: 데이터 조회 시 JSON 변환
# 역직렬화: 입력/업데이트 시 JSON → 객체 변환

from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin

from .models import Tag, Product, ProductOption


"""
기본적으로 상품 옵션, 태그, 상품 모델의 데이터를 직열화 및 역직열화 작업을 합니다.
상품 옵션은 제약이 없기때문이 기본적인 직열화가 가능한 ModelSerializer를 사용합니다.
태그 는 unique 제약이 존재합니다.
그럼으로 UniqueFieldsMixin 모듈을 사용해서 Create, Update 시 uniqueValidation 문제 를 해결합니다.
상품 은 직열화된 상품 옵션과 직열화된 태그 데이터를 중첩해서 사용해야 하기때문에 WritableNestedModelSerializer 모듈을 사용합니다.
"""


class ProductOptionSerializer(serializers.ModelSerializer):
    """상품 옵션 직렬화"""

    class Meta:
        model = ProductOption
        fields = ["pk", "name", "price"]


class TagSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    """태그 직렬화"""

    class Meta:
        model = Tag
        fields = ["pk", "name"]


class ProductSerializer(WritableNestedModelSerializer):
    """상품 직렬화 (옵션, 태그 포함)"""

    option_set = ProductOptionSerializer(many=True, required=False)
    tag_set = TagSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ["pk", "name", "option_set", "tag_set"]
