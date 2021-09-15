# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add gcc postgresql-dev python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .
RUN chmod 755 chamber
EXPOSE 8000
# run entrypoint.sh
#ENTRYPOINT ["./chamber", "exec", "todo/backend", "--"]
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]
