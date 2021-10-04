FROM nginx
RUN apt-get update
RUN apt-get install npm -y

# COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
WORKDIR /app

COPY ./package.json ./

RUN npm install

COPY ./ ./

RUN npm run build

EXPOSE 3000

CMD [ "npm", "run", "start" ]


