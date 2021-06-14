# FLASK DOCKERFILE FOR DEVELOPMENT

#obtenemos la imagen de un kernel de Linux con python
FROM python:3.8-alpine3.12

ENV PYTHONUNBUFFERED=1

RUN adduser -D -s /bin/sh app

# seleccionar la carpeta de usuario
WORKDIR /home/app

# copia la carpeta del proyecto a la imagen
ADD main ./main
ADD app.py .

#instala dependencias del sistema
RUN apk add build-base && \
    apk add mysql-client && \
    rm -rf /var/cache/apk/*

ADD requirements.txt ./requirements.txt

RUN python3 -m venv .
RUN source bin/activate
RUN pip3 install -r requirements.txt

USER app

#puerto por el que escucha la imagen
EXPOSE 5000

#ejecuta la aplicación
CMD [ "python", "./app.py" ]
