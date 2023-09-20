#!/bin/bash

apt update
apt install dpkg-dev devscripts equivs wget
cd nginx-1.20.1
ls -la
mk-build-deps --install
debuild -us -uc -b
ls ../
cd ..
dpkg -i nginx_1.20.1_amd64.deb
