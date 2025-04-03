# Base Image
FROM python:3.9-slim

# Update and Install Dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set Chrome and Chromedriver Path
ENV CHROMIUM_PATH=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set Working Directory
WORKDIR /app

# Copy Requirements and Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy All Files
COPY . .

# Start the Bot
CMD ["python", "main.py"]
