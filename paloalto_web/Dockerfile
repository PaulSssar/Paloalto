FROM python:3.11.3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "index:app", "--host", "0.0.0.0"]
