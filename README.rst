Python 2 Debian
===============

The goal of this project is to create a Debian package from a Python project using dh-virtualenv and Docker as build environment.

Requirements
------------

To build a Debian package the only requirement on your machine is Docker.

Build Debian package from a Python package:
-------------------------------------------

.. code:: bash

    docker run --rm -v /tmp/debs:/packages internap/python2debian \
        --package-name=almanach-api \
        --package-version=4.0.7 \
        --package-desc="Almanach is awesome" \
        --package-author="Internap Hosting <opensource@internap.com>" \
        --python-package="almanach==4.0.7"

Build Debian package from local source folder
---------------------------------------------

TODO

Build Docker image locally
--------------------------

.. code:: bash

    make image
