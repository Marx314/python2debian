FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir /build && \
    mkdir /packages && \
    echo "deb http://ppa.launchpad.net/spotify-jyrki/dh-virtualenv/ubuntu trusty main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 36A76C6C49C29687 && \
    apt-get -qq update && \
    apt-get -qq install -y build-essential libffi-dev libssl-dev devscripts python3 python-dev \
                           python-virtualenv python3-pip git equivs dh-virtualenv

COPY python2debian /usr/local/src/python2debian
COPY setup.py /usr/local/src/
COPY README.rst /usr/local/src/
COPY LICENSE /usr/local/src/

RUN cd /usr/local/src && python3 setup.py develop

ENTRYPOINT ["python3", "/usr/local/bin/python2debian"]
