FROM asia.gcr.io/kdd-txo-project/python-scikit:latest as base

LABEL maintainer “Kent Chen <N96061216@gs.ncku.edu.tw>”

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ADD . /crawler
WORKDIR /crawler

RUN ln -sf /usr/bin/python3 /usr/bin/python \
    && ln -sf /usr/bin/pip3 /usr/bin/pip

RUN apk update \
    && apk add --virtual build-deps g++ tzdata libc-dev libxslt-dev \
    && pip install --upgrade pip pipenv \
    && pipenv install --system --deploy \
    && cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime \
    && echo "Asia/Taipei" > /etc/timezone \
    && apk del build-deps

