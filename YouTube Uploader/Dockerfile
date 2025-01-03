# Use an ARM-compatible Python base image
FROM arm32v7/python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set up environment for YouTube upload (you'll need to configure this)
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json

# Run the application
CMD ["python", "youtube_uploader.py"]