image:
	@ docker build -t internap/python2debian .

push:
	@ docker push internap/python2debian:latest

exec:
	@ docker run -it internap/python2debian:latest bash

build-almanach:
	@ docker run --rm -v /tmp/debs:/packages internap/python2debian \
		--package-name=almanach-api \
    	--package-version="4.0.7" \
    	--package-desc="Almanach is awesome" \
    	--package-author="Internap Hosting <opensource@internap.com>" \
    	--python-package="almanach==4.0.7"
