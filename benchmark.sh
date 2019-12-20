#!/bin/bash
echo "Running health check benchmark..."
wrk2 -R 2000 -d 30 $1/healthz
