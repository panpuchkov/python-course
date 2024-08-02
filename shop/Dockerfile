FROM python:3.8

WORKDIR /app

# install and update required software
RUN apt-get update \
    && apt-get upgrade -y  --no-install-recommends \
    && apt-get install -y python3-psycopg2 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -U pip

# copy project source code and install project dependencies
COPY . /app
RUN pip install -r /app/requirements.txt

# set container working directory
EXPOSE 8000

# Run django application
ENTRYPOINT ["/app/run.sh"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
