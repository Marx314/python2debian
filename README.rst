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
        --package-desc="Almanach is awesome" \
        --package-author="Internap Hosting <opensource@internap.com>" \
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
        --package-desc="Almanach is awesome" \
        --package-author="Internap Hosting <opensource@internap.com>" \
        --python-package="almanach==4.0.7" \
        --postinst=/debian/almanach-api.postinst \
        --prerm=/debian/almanach-api.prerm \
        --file "/debian/almanach-api.upstart:/etc/init/almanach-api.conf" \
        --file "/debian/almanach-common.logrotate:/etc/logrotate.d/almanach"

Build Debian package from local source folder
---------------------------------------------

TODO

Build Docker image locally
--------------------------

.. code:: bash

    make image
