#!/bin/bash

apt update
apt install dpkg-dev devscripts equivs wget python3-distutils python-all python3-all
cd python-dateutil2.8.2
mk-build-deps --install
debuild -us -uc -b
cd ..
dpkg -i python3-dateutil_2.8.2_all.deb
