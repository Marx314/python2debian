FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir /build && \
    mkdir /packages && \
    mkdir /src && \
    echo "deb http://ppa.launchpad.net/spotify-jyrki/dh-virtualenv/ubuntu trusty main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 36A76C6C49C29687 && \
    apt-get -qq update && \
    apt-get -qq install -y build-essential libxml2-dev libffi-dev libssl-dev devscripts git equivs dh-virtualenv \
                           python3 python3-dev python3-pip libyaml-dev libmysqlclient-dev \
                           python-dev python-virtualenv

RUN pip install -U setuptools pip && pip3 install -U setuptools pip
RUN pip install -U cffi cryptography && pip3 install -U cffi cryptography

COPY python2debian /usr/local/src/python2debian
COPY setup.py /usr/local/src/
COPY README.rst /usr/local/src/
COPY LICENSE /usr/local/src/

RUN cd /usr/local/src && python3 setup.py develop

ENTRYPOINT ["python3", "/usr/local/bin/python2debian"]
