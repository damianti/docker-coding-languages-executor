### syntax=docker/dockerfile:1

# Use official Dart runtime as a parent image
FROM google/dart:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install flask

# Make port 5003 available to the world outside this container
EXPOSE 5003

# Run the application when the container launches
CMD ["python3", "dart-executor.py"]