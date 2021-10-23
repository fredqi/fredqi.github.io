#!/usr/bin/env bash
### setup_docker.sh ---
##
## Filename: setup_docker.sh
## Author: Fred Qi
## Created: 2020-08-16 11:17:34(+0800)
##
## Last-Updated: 2021-10-23 20:19:32(+0800) [by Fred Qi]
##     Update #: 20
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

## run one of following two commands to build website with jekyll
# docker exec jb jekyll build -s /srv/jekyll -d /srv/www
# docker exec jb bundle exec jekyll build -s /srv/jekyll -d /srv/www

######################################################################
### setup_docker.sh ends here
