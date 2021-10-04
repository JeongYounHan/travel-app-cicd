FROM nginx
RUN apt-get update
RUN apt-get install npm -y

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
WORKDIR /usr/share/nginx/html

COPY ./package.json ./

RUN npm install

COPY ./ ./

RUN npm run build

CMD [ "npm", "run", "start" ]


