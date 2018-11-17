FROM rackspacedot/python37
MAINTAINER Nerd-Bear "python@istruly.sexy"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

ENV SECRET_KEY="Nerd-Bear"
RUN pip3 install -r requirements.txt

WORKDIR /app/Server
