
FROM python:3.10-slim

# Set the working directory in the Docker image
WORKDIR /code

# Copy only the Flask server script into the container
COPY matrix_server.py /code/

# Copy the requirements.txt into the container at /code
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the server listens on
EXPOSE 5000

# Command to run the Flask server when the container launches
CMD ["python", "matrix_server.py"]