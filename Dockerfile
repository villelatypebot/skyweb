# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required by Playwright
RUN apt-get update && apt-get install -y \\
    wget \\
    gnupg \\
    ca-certificates \\
    fonts-liberation \\
    libappindicator3-1 \\
    libasound2 \\
    libatk-bridge2.0-0 \\
    libatk1.0-0 \\
    libcups2 \\
    libdbus-1-3 \\
    libdrm2 \\
    libgtk-3-0 \\
    libnspr4 \\
    libnss3 \\
    libx11-xcb1 \\
    libxcomposite1 \\
    libxdamage1 \\
    libxrandr2 \\
    xdg-utils \\
    libgbm1 \\
    libxss1 \\
    libgconf-2-4 \\
    libxkbcommon0 \\
    libgtk-4-1 \\
    libgraphene-1.0-0 \\
    libatomic1 \\
    libxslt1.1 \\
    libevent-2.1-7 \\
    libwebpdemux2 \\
    libharfbuzz-icu0 \\
    libenchant-2-2 \\
    libsecret-1-0 \\
    libhyphen0 \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium

# Copy the application code
COPY . .

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=src/main.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "src/main.py"]

