# Use the Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the calculator script into the container
COPY src/calculator.py /app/

# Install Flask and any other dependencies you might need
RUN pip install flask

# Expose the Flask app's port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "calculator.py"]
