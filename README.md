# 안녕하십니까
위 프로젝트는 오케이포스 코딩테스트 과제입니다.

## 프로젝트 목적
REST API 서버에서 중첩 데이터를 처리함에 용의한 DRF WritableNestedModelSerializer 모듈을 사용하는 방법과
models.py에서 컬럼에 unique값과 WritableNestedModelSerializer를 사용시 UniqueValidator 에서 값이 있으면 오류 를 발생함으로
데이터 생성 및 업데이트 과정에서 문제가 발생 하였습니다.
이를 해결하는 것이 과제라고 이해하였습니다.

## 해결
[https://github.com/beda-software/drf-writable-nested](https://github.com/beda-software/drf-writable-nested) 문서를 확인중
위 문제가 고질적인 문제이며 이를 해결하기 위해 UniqueFieldsMixin 를 Unique 값이 있는 Serializer에서 사용하면 값이 있으면 오류 에서 값이 있으면 연결로 변경 되어 생성 및 업데이트를 해결할수 있었습니다.

# 프로젝트 설치 및 진행 시나리오
## 1. 프로젝트 클론
```
git clone https://github.com/morakcook/okpose_assignment.git
cd okpose_assignment
```

## 2. Docker 이미지 빌드
```
docker build -t okpose_assignment .
```

## 3. 컨테이너 실행(Docker run)
```
docker run -d -p 8000:8000 okpose_assignment
```

## 3-2. Django runserver 실행 방법
```
#1. 프로젝트 이동
cd <프로젝트 디렉토리>
#2. 가상환경 실행
venv\Scripts\activate
#3. 서버 실행
python manage.py runserver
```

## 3-3. 접속 URL
## API URL

| 기능         | Method | URL                                                      |
| ------------ | ------ | -------------------------------------------------------- |
| 상품 생성      | POST   | [http://127.0.0.1:8000/shop/products/](http://127.0.0.1:8000/shop/products/) |
| 상품 목록 조회 | GET    | [http://127.0.0.1:8000/shop/products/](http://127.0.0.1:8000/shop/products/) |
| 상품 수정      | PATCH  | [http://127.0.0.1:8000/shop/products/1/](http://127.0.0.1:8000/shop/products/1/) |
| 특정 상품 조회 | GET    | [http://127.0.0.1:8000/shop/products/1/](http://127.0.0.1:8000/shop/products/1/) |


## DOC URL
```
[http://localhost:8000/doc/](http://localhost:8000/doc/)
```

## 4. Postman Export 결과
### 1. CREATE
```
{
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
            "name": "TestOption2",
            "price": 500
        },
        {
            "pk": 3,
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
            "pk": 2,
            "name": "NewTag"
        }
    ]
}
```

### 2. PATCH
```
{
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
            "pk": 4,
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
            "pk": 3,
            "name": "Edit New Tag"
        }
    ]
}
```

### 3. GET
```
[
    {
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
                "pk": 4,
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
                "pk": 3,
                "name": "Edit New Tag"
            }
        ]
    }
]
```

### 4. RETRIEVE
```
{
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
            "pk": 4,
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
            "pk": 3,
            "name": "Edit New Tag"
        }
    ]
}
```

### 5. POSTMAN EXPORT JSON
[Postman Export 파일 다운로드](okpose.postman_export.json)

## 5.  CODE COV 뱃지
[![codecov](https://codecov.io/github/morakcook/okpose_assignment/graph/badge.svg?token=E7AILJHUWX)](https://codecov.io/github/morakcook/okpose_assignment)

## 6. GITHUB ACTION 상태 뱃지
![CI](https://github.com/morakcook/okpose_assignment/actions/workflows/python-tests.yml/badge.svg)
