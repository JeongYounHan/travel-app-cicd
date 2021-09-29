# travel app upgrade

[![Actions Status](https://github.com/JeongYounHan/travel-app-cicd/workflows/docker/badge.svg)](https://github.com/JeongYounHan/travel-app-cicd/actions)

## 목차

1. [개요](#개요)

2. [업그레이드작업](#업그레이드작업)
   - [프론트엔드](#프론트엔드)
   - [docker CI/CD](#docker-CI/CD)

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
- CI/CD: docker, travis CI, AWS ElasticBeanstalk, nginx
- 테스트 툴: jest



## 업그레이드작업

### 프론트엔드

1. Vuetify 수정
2. 토큰 쿠키, env 수정
3. tdd



### docker CI/CD

Ci.cd 구조도



1. dockerfile / dockerfile.dev
   - Frontend - nuxt.js
   - Backend - Django(DB - sqlite)



2. Docker-compose



3. Travis.yml



4. Nginx





## 배운것







