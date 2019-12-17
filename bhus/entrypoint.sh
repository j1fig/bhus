#!/bin/bash

case "$1" in
    run)
        /src/server.py
        ;;
    test)
        mkdir -p $REPORTS_DIR
        pytest ${2:-} tests/
        ;;
    init-db)
        /src/init_db.py
        ;;
    *)
        exec "$@"
        ;;
esac
