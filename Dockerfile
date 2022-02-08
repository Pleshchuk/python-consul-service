FROM python

RUN pip3 install python-consul

COPY fyber-lab-consul-service.py /

RUN apt update && apt install -y iputils-ping

ENTRYPOINT [ "python3", "/fyber-lab-consul-service.py" ]