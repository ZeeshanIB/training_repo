FROM python:3.6-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN groupadd -g 999 webuser && \
    useradd -r -u 999 -g webuser webuser
COPY . .

EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]