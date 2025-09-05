# Dockerfile

# 1. Start with an official Python base image.
# 'python:3.9-slim' is a good choice as it's lightweight.
FROM python:3.9-slim

# 2. Set the working directory inside the container.
# This is where our app's code will live.
WORKDIR /app

# 3. Copy our Python script from our host machine into the container.
# The first '.' means the current directory on the host.
# The second '.' means the WORKDIR inside the container (/app).
COPY calculator.py .

# 4. Set the command to run when the container starts.
# This will execute 'python3 calculator.py' inside the container.
CMD ["python3", "calculator.py"]