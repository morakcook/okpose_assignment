# 베이스 이미지
FROM python:3.8-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 설치 (빌드용)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 의존성 설치
#1. requirements.txt 읽기
COPY requirements.txt .
#2. requirements.txt 내용 모듈들 설치
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 소스 복사
COPY . .

# 컨테이너 기본 명령
# 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
