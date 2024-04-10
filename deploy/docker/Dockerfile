# syntax = docker/dockerfile:experimental
FROM python:3.12

RUN apt-get update -y && apt-get install -y gnupg2 synaptic software-properties-common aptitude

RUN aptitude update                           && \
    aptitude upgrade -y                       && \
    aptitude install curl -y                  && \
    aptitude clean && aptitude autoclean       && \
    find /var/lib/apt/lists/ -type f -delete && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ bookworm-pgdg main 17" > /etc/apt/sources.list.d/pgdg.list                                && \
    curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -


RUN aptitude update && \
    aptitude install -y \
    libatlas-base-dev gfortran nginx nginx-extras postgresql-13 postgresql-client-13 supervisor

# COPY requirements /var/www/requirements
# RUN pip install --upgrade -r /var/www/requirements/requirements.txt

COPY sup /var/www/sup
COPY deployment/gunicorn/gunicorn_conf.py /var/www/

COPY deployment/nginx/nginx.conf /etc/nginx/nginx.conf
COPY deployment/supervisor/supervisord.conf /etc/supervisord.conf

RUN useradd sup && find /var/www -type f -exec chmod 755 {} \; && find /var/www -type d -exec chmod 755 {} \; && chown -R sup:sup /var/www

CMD ["/usr/bin/supervisord"]