FROM python:3
ADD requirements.txt .
ADD server.py .
RUN server.py