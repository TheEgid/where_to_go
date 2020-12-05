
FROM debian:bullseye

RUN apt-get update

RUN apt-get install -qy \
    apt-utils \
    python3-pip \
    gdal-bin \
    python3-psycopg2

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/services/djangoapp
WORKDIR /opt/services/djangoapp
COPY ./requirements.txt /opt/services/djangoapp

RUN pip install -r requirements.txt

COPY . /opt/services/djangoapp

EXPOSE 80

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":80", "--chdir", "where_to_go", "wsgi:application"]