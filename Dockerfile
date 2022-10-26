# syntax=docker/dockerfile:1

FROM python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY main.py /app/.
COPY query.py /app/.
COPY scrapy.py /app/.


CMD [ "flask","--debug", "run" , "--host=0.0.0.0"]