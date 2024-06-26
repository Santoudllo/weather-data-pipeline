
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


COPY script/app.py /app/script/app.py

CMD ["python", "/app/script/app.py"]
