# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app
COPY . /app

# Install the custom bashrc file
# COPY ./.bashrc .bashrc

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r alpha_scala_40/requirements.txt

# Install the alpha_scala_40 pyhton package
RUN pip3 install -e alpha_scala_40/.

RUN pip3 install pep8