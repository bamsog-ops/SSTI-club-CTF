# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all your files into the container
COPY . .

# Install dependencies
RUN pip install flask

# (Optional but safer) create non-root user
RUN useradd -m ctfuser
USER ctfuser

# Expose the port your app runs on
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
