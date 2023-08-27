# syntax=docker/dockerfile:1

FROM openjdk:8-jdk-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers python3 py3-pip && \
    pip3 install flask

COPY java-executor.py .

EXPOSE 5002

CMD [ "python3", "java-executor.py"]