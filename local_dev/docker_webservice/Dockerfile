FROM p0bailey/docker-flask
MAINTAINER Fuyang Liu "liufu.ty@gmail.com"

COPY flask.conf /etc/nginx/sites-available/

COPY app /var/www/app

CMD ["/usr/bin/supervisord"]
