FROM resin/rpi-raspbian:wheezy

RUN apt-get -q update && apt-get install -yq python python-pip python-dbus 

COPY . /app

CMD ['python', '/app/demo.py']
