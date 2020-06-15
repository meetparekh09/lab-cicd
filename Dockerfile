FROM python:3.7-alpine
WORKDIR /lab-docker
COPY . .
RUN pip install -r requirements.txt