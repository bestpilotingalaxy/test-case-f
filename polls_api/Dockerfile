FROM python:latest

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt app/requirements.txt

# RUN sudo apt-get update &&\
#     sudo apt-get upgrade -y &&\
#     pip3 install -U pip3 &&\
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app

CMD [ "python", "manage.py", "migrate"]