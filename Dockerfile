FROM python:3.9-slim AS build-image
ENV PYTHONDONTWRITEBYTECODE 1
ENV TERM xterm-256color
WORKDIR /code
COPY . /code/
RUN pip install pybuilder
RUN pyb install

FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV TERM xterm-256color
WORKDIR /opt/tfirmx
COPY --from=build-image /code/target/dist/tfirmx-*/dist/tfirmx-*.tar.gz /opt/tfirmx
RUN pip install tfirmx-*.tar.gz
ENTRYPOINT ["tfirmx"]