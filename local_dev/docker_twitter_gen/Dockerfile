FROM python:2.7

RUN pip install tweepy
RUN pip install yoyo-migrations
RUN pip install psycopg2

COPY twitter_gen /twitter_gen
VOLUME ["/twitter_gen/log"]

WORKDIR /twitter_gen

CMD ["python", "twitter_stream_download.py"]
