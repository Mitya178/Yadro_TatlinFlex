#!/bin/bash

dnf update
yum install rpmdevtools rpmlint rpm-build
yum group install "Development Tools"
rpmdev-setuptree





cd python-dateutil2.8.2

