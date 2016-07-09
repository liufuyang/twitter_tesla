FROM python:2.7

RUN pip install tweepy
COPY twitter_gen /twitter_gen

WORKDIR /twitter_gen

CMD ["/bin/bash", "gen.sh"]
