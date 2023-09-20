#!/bin/bash

apt update
apt install dpkg-dev devscripts equivs wget python3-all, python3-setuptools, python3-six
cd python-dateutil2.8.2
ls -la
mk-build-deps --install
debuild -us -uc -b
ls ../
cd ..
dpkg -i python-dateutil-build-deps_2.8.2_all.deb
