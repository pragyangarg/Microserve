FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install fastapi \
    uvicorn \
    sqlalchemy \
    psycopg2-binary \
    passlib[bcrypt] \
    bcrypt==4.0.1 \
    python-jose[cryptography] \
    httpx

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
