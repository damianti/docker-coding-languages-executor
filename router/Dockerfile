FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip3 install flask requests

COPY router.py .

EXPOSE 5005

# Start the terminal when the container is run
CMD [ "python3", "router.py"]