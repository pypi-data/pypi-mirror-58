#!/bin/bash

ME=$(readlink -f "$0")
MYDIR=$(dirname "$ME")

LOGFILE="DOCKER-RUN.LOG"

cd "$MYDIR"

images=$(./docker-build.sh | grep '^\(debian\|fedora\)')

rm -f $LOGFILE

for img in $images; do
    ./docker-run.sh $img
done
