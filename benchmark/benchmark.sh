#!/bin/bash

docker run -it --rm -v `pwd`/conf:/opt/gatling/conf \
    -v `pwd`/user-files:/opt/gatling/user-files \
    -v `pwd`/results:/opt/gatling/results \
    --network="host" \
    denvazh/gatling
