# build stage
FROM node:alpine as builder

WORKDIR /app

COPY ./package.json ./

RUN npm install

COPY ./ ./

RUN npm run build
    
# run stage

FROM nginx 

EXPOSE 3000

# 내가 작성한 것으로 nginx 설정 대체, 웹서버 설정파일
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf 
# 위의 builder 에서 빌드된 파일 복사
COPY --from=builder /app/.nuxt /usr/share/nginx/html
# nuxt 정적파일
CMD [ "npm", "run", "start" ]

