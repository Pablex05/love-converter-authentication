#obtenemos la imagen de un kernel de Linux con python
FROM python:3.8-alpine3.12

ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flaskapp/.local/bin

RUN mkdir /home/flaskapp
#crea usuario
RUN adduser -S -D -H flaskapp

RUN chown -R flaskapp /home/flaskapp

#seleccionar la carpeta de usuario
WORKDIR /home/flaskapp

RUN mkdir main
#copia la carpeta del proyecto a la imagen
COPY ./main ./main
COPY ./app.py .

#instala dependencias del sistema
RUN apk add --update curl gcc g++ libffi-dev openssl-dev build-base linux-headers && \
    apk add mysql-client && \
    apk add postgresql-client && \
    rm -rf /var/cache/apk/*

ADD requirements.txt ./requirements.txt
USER flaskapp
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gevent gunicorn==20.1.0

#puerto por el que escucha la imagen
EXPOSE 5000

#HEALTHCHECK --interval=10s --timeout=10s --start-period=55s CMD \ 
#curl -f --retry 10 --max-time 15 --retry-delay 10 --retry-max-time 60 "http://localhost:8080/api/health" || exit 1   

