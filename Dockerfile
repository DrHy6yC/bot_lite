FROM python:3.11-alpine3.22

LABEL authors="drhy6"

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["python", "bot/main.py"]
