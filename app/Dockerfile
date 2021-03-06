# Pull official Python3.8.1 Docker Image
FROM python:3.8.1-alpine

# Set wroking directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install psycopg2 dependencies - For using PostgreSQL
RUN apk update \
    && apk add postgresql-dev \
               gcc \
               python3-dev \
               musl-dev \
               # Pillow Dependencies
               jpeg-dev \
               zlib-dev \
               freetype-dev \
               lcms2-dev \
               openjpeg-dev \
               tiff-dev \
               tk-dev \
               tcl-dev \
               harfbuzz-dev \
               fribidi-dev


# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements_dev.txt .
RUN pip install -r requirements_dev.txt

# Copy endtypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy project code
COPY . /usr/src/app/

EXPOSE 8000

# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]