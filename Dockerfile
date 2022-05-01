FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y git wget software-properties-common build-essential manpages-dev curl iputils-ping vim htop\
    && add-apt-repository ppa:dqlite/dev -y \ 
    && apt-get update \
    && apt-get install -y golint libsqlite3-dev libuv1-dev liblz4-dev libraft-dev libdqlite-dev

RUN wget -c https://golang.org/dl/go1.15.2.linux-amd64.tar.gz \
    && shasum -a 256 go1.15.2.linux-amd64.tar.gz \
    && tar -C /usr/local -xvzf go1.15.2.linux-amd64.tar.gz 

ENV PATH="/root/go/bin:/usr/local/go/bin:${PATH}"

ADD tool/crash-raft1.sh /crash-raft1.sh
ADD tool/crash-raft2.sh /crash-raft2.sh
ADD go-dqlite-master /go-dqlite

RUN export CGO_LDFLAGS_ALLOW="-Wl,-z,now" \
    && cd go-dqlite \ 
    && go build -tags libsqlite3 \ 
    && go install -tags libsqlite3 ./cmd/dqlite-demo \ 
    && go install -tags libsqlite3 ./cmd/dqlite-benchmark  
