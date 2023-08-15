# Use an official Python runtime as the parent image
FROM python:3.8.0

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["gunicorn", "lets_vote.wsgi:application", "--bind", "0.0.0.0:8000"]
