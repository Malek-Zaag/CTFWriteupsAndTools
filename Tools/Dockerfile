FROM ubuntu:24.04

ENV DEBIAN_FRONTEND noninteractive


RUN apt update --fix-missing
RUN apt install build-essentials
RUN apt install -y git wget patchelf file strace tmux python3 golang
RUN apt install -y netcat python3-pip ruby-full valgrind vim xclip elfutils
RUN apt install -y make
RUN apt install default-jre default-jdk nodejs npm


WORKDIR /app
CMD bash