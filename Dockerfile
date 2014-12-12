FROM resin/rpi-raspbian:wheezy

RUN apt-get -q update && apt-get install -yq python python-dbus --no-install-recommends

COPY . /app

CMD ["python", "/app/demo.py"]
