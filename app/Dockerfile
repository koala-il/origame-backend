# Pull official Python3.8.1 Docker Image
FROM python:3.8.1-alpine

# Set wroking directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install psycopg2 dependencies - For using PostgreSQL
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy endtypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy project code
COPY . /usr/src/app/

# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]