FROM debian:stretch
MAINTAINER Aatoli Che <anatoli.che@gmail.com>

RUN apt-get update > /dev/null &&  DEBIAN_FRONTEND=noninteractive apt-get -y -q install \
    vim screen python3-pip locales procps tmux

RUN pip3 install pika pyyaml
RUN pip3 install python-telegram-bot apiai

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
RUN sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:en
ENV LC_ALL ru_RU.UTF-8



COPY src/bot.py /opt/
COPY src/bot.sh /opt/

RUN adduser --disabled-password --gecos "" pybot
WORKDIR /home/pybot
USER pybot



ENTRYPOINT ["/opt/bot.sh"]
#CMD ["/opt/bot.sh"]

