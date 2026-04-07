# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port that Flask runs on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
