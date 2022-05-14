FROM python:3.8

# Install project package
WORKDIR /home/mydatastudio

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt 

RUN echo "Collect static files" && python manage.py collectstatic --noinput
RUN echo "Make migrations" && python manage.py makemigrations  \
                           && python manage.py makemigrations blog  \
                           && python manage.py makemigrations products
RUN echo "Apply database migrations" && python manage.py migrate

ENV PORT 8080
EXPOSE 8080

RUN mkdir logs 

CMD gunicorn mydatastudio.wsgi:application \
    --name mydatastudio \
    --workers 2 \
    --bind :$PORT \
    --log-level=debug \
    --access-logfile=/home/mydatastudio/logs/gunicorn_access.log \
    --error-logfile=/home/mydatastudio/logs/gunicorn_error.log
