image:
	@ docker build -t internap/python2debian .

push:
	@ docker push internap/python2debian:latest

exec:
	@ docker run -it internap/python2debian:latest bash
