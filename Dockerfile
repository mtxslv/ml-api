FROM python:3.11.9-bookworm
RUN apt-get update -y 
WORKDIR /app

# Create folders
RUN mkdir ./models
RUN mkdir ./src
RUN mkdir ./src/service

# Copy 
COPY src/service ./src/service
COPY requirements.txt ./requirements.txt
COPY models/ ./models

# install dependencies
RUN pip install -r requirements.txt

# run hypercorn
ENTRYPOINT ["hypercorn", "src.service.entrypoints.api:app", "-b", "0.0.0.0:8080"]