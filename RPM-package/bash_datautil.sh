#!/bin/bash

dnf update
yum install rpmdevtools rpmlint rpm-build
yum group install "Development Tools"
yum-builddep rpmbuild/SPECS/pg_redis_pubsub.spec

rpmlint rpmbuild/SPECS/pg_redis_pubsub.spec
rpmbuild -bb rpmbuild/SPECS/pg_redis_pubsub.spec
