FROM openjdk:8-jdk

ENV TINI_VERSION v0.13.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN useradd -ms /bin/bash android

RUN mkdir -p /home/android && \
    chown -R android:android /home/android
