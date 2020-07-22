FROM python:3.8
WORKDIR /code
COPY ./ ./
RUN pip install -r requirements.txt
RUN pip install uwsgi
CMD uwsgi --http :9600 --wsgi-file gremlin_proxy/wsgi.py --master --processes 4 --threads 2


