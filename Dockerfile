FROM debian:bullseye

RUN apt-get update

ENV PYTHONUNBUFFERED 1

RUN apt-get install -qy \
    apt-utils \
    python3.9 python3-pip \
    wget python3-psycopg2

RUN apt-get install -qy \
    gdal-bin libgdal-dev \
    binutils libproj-dev

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-`dpkg --print-architecture`-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-`dpkg --print-architecture`-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-`dpkg --print-architecture`-$DOCKERIZE_VERSION.tar.gz

RUN mkdir -p /opt/services/djangoapp
WORKDIR /opt/services/djangoapp
COPY ./requirements.txt /opt/services/djangoapp

RUN pip install -r requirements.txt

COPY . /opt/services/djangoapp

EXPOSE 80

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":80", "--chdir", "where_to_go", "wsgi:application"]