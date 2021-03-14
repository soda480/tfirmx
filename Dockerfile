FROM python:3.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1
ENV TERM xterm-256color

WORKDIR /tfirmx

COPY . /tfirmx/
RUN apk --update --no-cache add gcc libc-dev libffi-dev openssl-dev
RUN pip install twine
RUN pip install pybuilder
