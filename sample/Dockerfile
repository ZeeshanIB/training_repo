FROM python:3.8.3-slim-buster
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirments.txt
CMD ["python", "app.py"]
