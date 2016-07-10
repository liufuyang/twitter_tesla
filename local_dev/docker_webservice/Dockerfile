FROM liufuyang/flask
MAINTAINER Fuyang Liu "liufu.ty@gmail.com"

COPY flask.conf /etc/nginx/sites-available/

COPY app /var/www/app
RUN mkdir -p /var/www/app/log

CMD ["/usr/bin/supervisord"]
