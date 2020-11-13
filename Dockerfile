FROM python:latest

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt app/requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
   
COPY . /app

CMD [ "python", "manage.py", "migrate"]