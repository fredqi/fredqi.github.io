#!/usr/bin/env bash

# docker run -v `pwd`/vendor/bundle:/usr/local/bundle -v `pwd`/fredqi.github.io:/srv/jekyll -v `pwd`/gh-pages-fredqi:/srv/www -p 4000:4000 -it --rm jekyll/jekyll .config/build.sh

## Initialize the bundler environment
gem sources --add https://mirrors.tuna.tsinghua.edu.cn/rubygems/ --remove https://rubygems.org/
# bundle config set --local mirror.https://rubygems.org https://mirrors.tuna.tsinghua.edu.cn/rubygems
# bundle config set --local path /usr/local/bundle
bundle install

bundle exec jekyll serve -H 0.0.0.0 -d /srv/www

## Other commands
# bundle exec jekyll build -d /srv/www
