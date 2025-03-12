# Use the official Python image from Docker Hub
FROM python:3.9-alpine

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    tesseract-ocr \
    && pip install --no-cache-dir --upgrade pip

# Install pipenv to manage dependencies from Pipfile.lock
RUN pip install pipenv

# Set the working directory inside the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Install dependencies using pipenv (from Pipfile.lock)
RUN pipenv install --deploy --ignore-pipfile

# Copy the application code into the container
COPY ./app /app

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
