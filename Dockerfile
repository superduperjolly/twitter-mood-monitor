FROM python:3.6.0-slim

# Install packages
RUN pip install pipenv==2018.11.26
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system

# Maintain the working directory
WORKDIR /twitter-mood-monitor

# Copy the app files
COPY . /twitter-mood-monitor

# Expose a port to communicate with the outside world
EXPOSE 5000

# Let's make this an executable Python image, whatever happens
ENTRYPOINT ["python"]

# Write the default command here
CMD ["run.py"]
