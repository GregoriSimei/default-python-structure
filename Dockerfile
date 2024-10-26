FROM python:3.13.0-slim

RUN apt-get update && apt-get install git -y

WORKDIR /app/python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD tail -f /dev/null
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]