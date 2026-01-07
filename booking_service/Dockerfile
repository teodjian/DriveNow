# UPDATE: Using Python 3.14
FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into the package folder structure
COPY . ./booking_service

ENV PYTHONPATH=/app

CMD ["python", "-m", "booking_service.main"]