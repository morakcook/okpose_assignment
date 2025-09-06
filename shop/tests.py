import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_product_full_crud():
    # 테스트용 클라이언트 연동
    client = APIClient()


    # URL 엔드포인트를 사용한 CRUD url들 생성
    create_url = reverse("product-list")
    patch_url = reverse("product-detail", args=[1])
    list_url = reverse("product-list")
    retrieve_url = reverse("product-detail", args=[1])


    # CRUD 용 데이터
    create_data = {
        "name": "TestProduct",
        "option_set": [
            {
                "name": "TestOption1", 
                "price": 1000
             },
            {
                "name": "TestOption2", 
                "price": 500
            },
            {
                "name": "TestOption3", 
                "price": 0
            }
        ],
        "tag_set": [
            {
                "pk": 1,
                "name": "ExistTag"
            },
            {
                "name": "NewTag"
            }
        ]
    }
    patch_data = {
        "pk": 1,
        "name": "TestProduct",
        "option_set": [
            {
                "pk": 1,
                "name": "TestOption1",
                "price": 1000
            },
            {
                "pk": 2,
                "name": "Edit TestOption2",
                "price": 1500
            },
            {
                "name": "Edit New Option",
                "price": 300
            }
        ],
        "tag_set": [
            {
                "pk": 1,
                "name": "ExistTag"
            },
            {
                "pk": 2,
                "name": "NewTag"
            },
            {
                "name": "Edit New Tag"
            }
        ]
    }

    #1. 생성(CREATE)
    create_resp = client.post(create_url, create_data, format="json")
    assert create_resp.status_code == 201


    #2. 업데이트(PATCH)
    patch_resp = client.patch(patch_url, patch_data, format="json")
    assert patch_resp.status_code == 200


    #3. 목록 불러오기(GET)
    list_resp = client.get(list_url)
    assert list_resp.status_code == 200


    #4. 특정 데이터(pk=1) 불러오기(RETRIVE)
    retrieve_resp = client.get(retrieve_url)
    assert retrieve_resp.status_code == 200
