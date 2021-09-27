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

# 내가 작성한 것으로 nginx 설정 대체
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf 
COPY --from=builder /app/.nuxt /usr/share/nginx/html

