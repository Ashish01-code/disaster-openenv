FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all project files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run baseline script
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
