Python 2 Debian
===============

The goal of this project is to create a Debian package from a Python project using dh-virtualenv and Docker as build environment.

Requirements
------------

- To build a Debian package the only requirement on your machine is Docker.
- The Docker image is **not rebuilt each time**.

Build Debian package from a Python package:
-------------------------------------------

Use the argument :code:`python-package`:

.. code:: bash

    docker run --rm -v /tmp/debs:/packages internap/python2debian \
        --package-name=almanach-api \
        --package-version=4.0.7 \
        --package-desc="Almanach is awesome" \
        --package-author="Internap Hosting <opensource@internap.com>" \
        --python-package="almanach==4.0.7"

.. code:: bash

    ls /tmp/debs/
    almanach-api_4.0.7_amd64.deb

Build package with custom hooks (prerm, postinst, etc.)
-------------------------------------------------------

.. code:: bash

    docker run --rm \
        -v /tmp/debs:/packages \
        -v /my/local/debian_folder:/debian \
        internap/python2debian \
        --package-name=almanach-api \
        --package-version=4.0.7 \
        --python-package="almanach==4.0.7" \
        --postinst=/debian/almanach-api.postinst \
        --prerm=/debian/almanach-api.prerm

Build package with additional files
-----------------------------------

.. code:: bash

    docker run --rm \
        -v /tmp/debs:/packages \
        -v /my/local/debian_folder:/debian \
        internap/python2debian \
        --package-name=almanach-api \
        --package-version=4.0.7 \
        --python-package="almanach==4.0.7" \
        --postinst=/debian/almanach-api.postinst \
        --prerm=/debian/almanach-api.prerm \
        --file "/debian/almanach-api.upstart:/etc/init/almanach-api.conf" \
        --file "/debian/almanach-common.logrotate:/etc/logrotate.d/almanach"

Build Debian package from local source folder
---------------------------------------------

Use the argument :code:`source-dir`. The project must have a :code:`setup.py` and optionally a :code:`debian` folder.

.. code:: bash

    docker run --rm \
        -v /tmp:/packages \
        -v /my/local/source/folder:/src \
        internap/python2debian \
        --package-name=myapp \
        --package-version=42 \
        --source-dir=/src

Use another version of Python
-----------------------------

Use the arguments :code:`python-version` and :code:`python-bin`.

.. code:: bash

    docker run --rm \
        -v /tmp:/packages \
        -v /my/local/source/folder:/src \
        internap/python2debian \
        --package-name=myapp \
        --package-version=42 \
        --python-version=python3.4 \
        --python-bin=/usr/bin/python3.4 \
        --source-dir=/src

Build Docker image locally
--------------------------

.. code:: bash

    make image
