# syntax=docker/dockerfile:1

FROM python:3.8-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip3 install flask

COPY python-executor.py .

EXPOSE 5001

CMD [ "python3", "python-executor.py"]
