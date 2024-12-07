FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "/app/academic_performance/manage.py", "runserver", "0.0.0.0:8000"]