#!/bin/bash

case "$1" in
    run)
        /src/run
        ;;
    test)
        mkdir -p $REPORTS_DIR
        pytest ${2:-} tests/
        ;;
    *)
        exec "$@"
        ;;
esac
