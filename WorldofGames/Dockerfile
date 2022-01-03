FROM python:3.8-alpine

CMD EXPORT CFLAGS=-Qunused-arguments
CMD EXPORT CPPFLAGS=-Qunused-arguments
COPY . /wog
WORKDIR /wog
RUN pip install --upgrade pip
RUN pip install -r /wog/requirements.txt
RUN ls /wog
