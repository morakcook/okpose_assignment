# okpose_assignment
오케이포스 코딩테스트 과제입니다.


## 프로젝트 클론
```
git clone https://github.com/morakcook/okpose_assignment.git
cd okpose_assignment
```

## Docker 이미지 빌드
```
docker build -t okpose_assignment .
```

## 컨테이너 실행
```
docker run -d -p 8000:8000 okpose_assignment
```

## API URL
```
상품 리스트 GET, POST: http://localhost:8000/shop/product/
상품 PATCH: http://localhost:8000/shop/product/1/
API 문서: http://localhost:8000/doc/
```

## CODE COV 뱃지
[![codecov](https://codecov.io/github/morakcook/okpose_assignment/graph/badge.svg?token=E7AILJHUWX)](https://codecov.io/github/morakcook/okpose_assignment)