# travel app upgrade

## 목차

1. [개요](#개요)

2. [작업과정](#작업과정)
   - [프론트엔드](#프론트엔드)
   - [docker&CI/CD](#docker&CI/CD)

3. [배운것](#배운것)

## 개요

#### 기간

2021.09.22 ~ 될때까지



#### 목적: 예전에 만든 프로젝트 업그레이드

1. 도커로 CI/CD, Nginx 적용
2. 토큰 쿠키, env 등 프로젝트 세팅 수정
3. tdd로 핵심 코드(일정 드래그 앤 드롭으로 순서 정하기, 맵핑) 다시 코딩
4. vuetify 버전 올라가며 deprecated 된 부분 수정



#### 기술 스택

- 프론트엔드: nuxt (vue, vuex), vuetify
- 백엔드: django(sqlite)
- CI/CD: docker, GitHub actions, AWS EC2, nginx
- 테스트 툴: jest



#### 결과

http://3.34.199.215



## 작업과정

### 프론트엔드

1. Vuetify 수정
2. 토큰 쿠키, env 수정
3. tdd



### docker&CI/CD

Ci.cd 구조도



1. dockerfile(production)
   - Frontend - nuxt.js
   
     ```dockerfile
     FROM node:alpine
     
     WORKDIR /app
     
     COPY ./package.json ./
     
     RUN npm install
     
     COPY ./ ./
     
     RUN npm run build
     
     ENV HOST 0.0.0.0
     EXPOSE 3000
     
     CMD [ "npm", "run", "start" ]
     ```
   
     
   
   - Backend - Django(DB - sqlite)
   
     ```dockerfile
     FROM python:3.6
     
     WORKDIR /app
     
     COPY ./requirements.txt ./
     
     RUN pip install -r requirements.txt
     
     COPY . .
     
     CMD ["python", "manage.py", "migrate"]
     
     EXPOSE 8000
     
     CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
     ```
   
     
   
   - Nginx
   
     ```dockerfile
     FROM nginx
     COPY ./default.conf /etc/nginx/conf.d/default.conf
     ```
   
     

2. Docker-compose

   ```yaml
   version: "3"
   services: 
     frontend:
       image: 51sarang/docker_front
     nginx:
       restart: always # nginx는 소중하니깐
       image: 51sarang/docker_nginx
       ports:
         - "80:80"
       links:
         - frontend
         - backend
       depends_on : 
         - backend
     backend:
       image: 51sarang/docker_back
   ```



3. github actions yml

   ```yaml
   name: Docker CI/CD Pipeline
   
   on:
     push:
       branches: [ main ]
   
   jobs:
     continuous-integration:
       runs-on: ubuntu-latest
   
       steps:
       - uses: actions/checkout@v2
   
       - name: Login to dockerhub
         run: docker login -u ${{ secrets.DOCKER_USERNAME }} -p ${{ secrets.DOCKER_PASSWORD }}
       
       - name: Build Docker Dev Front
         run: docker build -t ${{ secrets.DOCKER_USERNAME }}/docker_front -f ./front/Dockerfile.dev ./front
       
   #     - name: Run Test
   #       run: docker run -e CI=true ${{ secrets.DOCKER_USERNAME }}/docker_front npm run test -- --coverage
       
       - name: Build Docker Front image
         run: docker build -t ${{ secrets.DOCKER_USERNAME }}/docker_front ./front
       - name: Build Docker Back image
         run: docker build -t ${{ secrets.DOCKER_USERNAME }}/docker_back ./back
       - name: Build Docker Nginx image
         run: docker build -t ${{ secrets.DOCKER_USERNAME }}/docker_nginx ./nginx
       - name: Push Docker Front image to DockerHub
         run: docker push ${{ secrets.DOCKER_USERNAME }}/docker_front
       - name: Push Docker Back image to DockerHub
         run: docker push ${{ secrets.DOCKER_USERNAME }}/docker_back
       - name: Push Docker Nginx image to DockerHub
         run: docker push ${{ secrets.DOCKER_USERNAME }}/docker_nginx
             
           
     continuous-deployment:
       runs-on: ubuntu-latest
       needs: [continuous-integration]
       steps:
         - name: Configure AWS credentials
           uses: aws-actions/configure-aws-credentials@v1
           with:
             aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
             aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
             aws-region: ap-northeast-2
             
         - name: Create CodeDeploy Deployment
           id: deploy
           run: |
             aws deploy create-deployment \
               --application-name Git_Application \
               --deployment-group-name development_gropup \
               --deployment-config-name CodeDeployDefault.OneAtATime \
               --github-location repository=${{ github.repository }},commitId=${{ github.sha }}
   ```
   
   

4. Nginx

   - default.conf

   ```
   upstream frontend {
     server frontend:3000;
   }
   upstream backend {
     server backend:8000;
   }
   
   server {
     listen 80;
   
     location / {
       proxy_pass http://frontend;
     }
   
     location /api {
       proxy_pass http://backend;
     }
   
     location /rest-auth {
       proxy_pass http://backend;
     }
   }
   ```

   



## 배운것







