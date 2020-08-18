#!/usr/bin/env bash
### setup_docker.sh ---
##
## Filename: setup_docker.sh
## Author: Fred Qi
## Created: 2020-08-16 11:17:34(+0800)
##
## Last-Updated: 2020-08-16 11:23:48(+0800) [by Fred Qi]
##     Update #: 16
######################################################################
##
### Commentary:
##
##
######################################################################
##
### Change Log:
##
##
######################################################################

cd ~/github/webpage

docker run --name www \
       -v `pwd`/gh-pages-fredqi:/usr/share/nginx/html/ \
       -d -p 80:80 nginx:latest

docker create --name jb \
       -v `pwd`/fredqi.github.io:/srv/jekyll \
       -v `pwd`/gh-pages-fredqi:/srv/www \
       -it jekyll/jekyll:latest bash

docker start jb

docker exec jb bundle config --local mirror.https://rubygems.org https://gems.ruby-china.com
docker exec jb bundle config --local development true
docker exec jb bundle config --local path vendor/bundle


######################################################################
### setup_docker.sh ends here
