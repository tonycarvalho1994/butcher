FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev \
    gcc

RUN apt-get install -y --reinstall build-essential

RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 8000

CMD ["python", "-m", "app.infra.http.fastapi.__init__"]
