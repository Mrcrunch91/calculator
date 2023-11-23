FROM ubuntu:latest

USER root

RUN apt -qy update && apt -qy upgrade
RUN apt -qy install python3
RUN apt -qy install python3-pip
COPY . /home/jenkins/
RUN pip3 install -r /home/jenkins/requirements.txt
ENTRYPOINT ["python3", "/home/jenkins/book_library.py"]