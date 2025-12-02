FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir Flask==2.3.3

COPY app/ /app/

EXPOSE 5000

CMD ["python","app.py"]


