FROM python:2.7.9

MAINTAINER Hypo i@ihypo.net

RUN mkdir /wechat
WORKDIR /wechat
COPY . /wechat

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py"]

EXPOSE 5000
