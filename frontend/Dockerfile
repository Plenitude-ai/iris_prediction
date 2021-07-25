FROM python:3.8

RUN apt-get update && apt-get install -y


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
# RUN pip3 install --upgrade pip==20.0.1DOCKER 
RUN pip install -r requirements.txt
COPY . /app

# # This is for the docker compose
ARG PORT
EXPOSE $PORT
VOLUME ["/app"]

# ENTRYPOINT [ "python" ]
# CMD ["src/main.py"]



# For heroku
# The --chdir allows to place the command from the folder you want (kind of a WORKDIR function)
# CMD gunicorn --chdir src main:app -b 0.0.0.0:$PORT
CMD gunicorn flask_server:app -b 0.0.0.0:$PORT --reload


