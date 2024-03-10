#!/bin/bash

docker build -f Dockerfile \
        -t ocallaje/nextflow_monitor:0.1 \
        $(for i in `cat .env`; do out+="--build-arg $i " ; done; echo $out;out="") .