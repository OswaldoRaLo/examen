FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir Flask Flask-MongoEngine gunicorn

EXPOSE 5000

CMD ["python", "api.py"]

