FROM node:6

ENV TINI_VERSION v0.13.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN mkdir -p /home/node && \
    chown -R node:node /home/node

ENV NODE_PATH /usr/local/lib/node_modules
RUN apt-get update
RUN apt-get -y install python-pip python-dev python-virtualenv git
RUN echo 'source ~/aws/env/bin/activate' >> /etc/profile.d/awscli.sh
USER node
RUN mkdir ~/aws && \
    virtualenv ~/aws/env && \
    ~/aws/env/bin/pip install awscli
RUN . ~/aws/env/bin/activate && \
    aws configure set preview.cloudfront true
