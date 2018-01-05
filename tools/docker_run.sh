#!/bin/sh

docker build -t foe .
docker run --rm \
   --interactive --tty \
   --security-opt seccomp:unconfined \
   --volume $PWD/../:/home/user/foe \
   foe tmux
