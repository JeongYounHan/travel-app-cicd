FROM node:16-alpine3.12

# COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
WORKDIR /app

COPY ./package.json ./

RUN npm install

COPY ./ ./

RUN npm run build

ENV HOST 0.0.0.0
EXPOSE 3000

CMD [ "npm", "run", "start" ]


