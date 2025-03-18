FROM python:3.11-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./farewell.env .
RUN pip install -r farewell.env

COPY ./entrypoint.sh .
COPY ./cert.crt .
COPY ./cert.key .
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]