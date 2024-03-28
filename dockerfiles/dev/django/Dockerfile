# Pull base image
FROM python:3.10-slim-buster  
#==> pull python image


LABEL maintainer="jahediman@gmail.com"

#Set Environment variables
ENV PYTHONUNBUFFRED=1
# ENV PYTHONDONTWRITEBYTECODE=1

# Set Working Directory
WORKDIR /usr/src/app   
#! set a path of directory to copy all project into it

# Install Dependencies
COPY ./requirements.txt .
# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project file to container
COPY ./core .

# copy project directory to working directory in container
# our project in core directory so copy ./core to . that is working directory
