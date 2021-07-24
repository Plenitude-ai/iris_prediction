FROM python:3.8

RUN apt-get update && apt-get install -y


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
# RUN pip3 install --upgrade pip==20.0.1DOCKER 
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 5000
VOLUME ["/app"]

# ENTRYPOINT [ "python" ]
# CMD ["src/main.py"]

# For heroku
CMD ["./gunicorn_starter.sh"]


