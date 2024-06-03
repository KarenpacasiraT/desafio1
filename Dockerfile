FROM python:3.8-slim

WORKDIR /app

COPY requerimientos.txt requerimientos.txt
RUN pip install -r requerimientos.txt

COPY app app

CMD ["python", "app/app.py"]
