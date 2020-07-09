# start from an official image
FROM python:3.7-alpine

RUN mkdir -p /home/CachePrep
COPY requirements.txt /requirements.txt
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps
RUN pip install -r /requirements.txt

COPY ./CachePrep /home/CachePrep
WORKDIR /home/CachePrep

# expose the port 8002
EXPOSE 8002

