FROM p0bailey/docker-flask
MAINTAINER Fuyang Liu "liufu.ty@gmail.com"

RUN apt-get update
RUN apt-get install -y libpq-dev
RUN pip install psycopg2

CMD ["/usr/bin/supervisord"]
