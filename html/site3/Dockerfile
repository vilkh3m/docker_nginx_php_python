FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY gunicorn.conf.py .

CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]