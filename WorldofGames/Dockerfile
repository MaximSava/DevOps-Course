FROM python:3.8-slim

COPY . /wog
WORKDIR /wog
RUN apt-get update
RUN pip install --upgrade pip
RUN apt-get -y install gcc
RUN pip install -r /wog/requirements.txt
CMD python MainScores.py
