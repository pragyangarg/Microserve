FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install fastapi \
    uvicorn \
    sqlalchemy \
    psycopg2-binary \
    python-jose[cryptography]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]