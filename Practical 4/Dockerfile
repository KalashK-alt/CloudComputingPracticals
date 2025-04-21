# Use official Python image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install Pillow

# Copy the script
COPY resizeNew.py .

# Command to run the script
ENTRYPOINT ["python", "resizeNew.py"]
