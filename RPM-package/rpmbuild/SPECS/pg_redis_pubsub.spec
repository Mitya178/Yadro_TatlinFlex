Name:           pg_redis_pubsub
Version:        1.0.2
Release:        1%{?dist}
Summary:        Redis Publish from PostgreSQL
License:        X11 License
URL:            https://github.com/brettlaforge/pg_redis_pubsub
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  postgresql-devel postgresql-server-devel
BuildRequires:  hiredis-devel
Requires:       postgresql
%if 0%{?rhel} < 8
Requires:       hiredis-last >= 0.13.3-1
%else
Requires:       hiredis = 0.15
%endif

%define         _build_id_links none

%description
Redis Publish from PostgreSQL

%prep
%{__rm} -rf %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
%{__tar} -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version} --strip-components 1

%build
cd %{name}-%{version}
%{__make}

%install
cd %{name}-%{version}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf $RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_DIR/*

%files
%defattr(-,root,root)
%{_libdir}/pgsql/redis.so
%{_datadir}/pgsql/extension/redis.control
%{_datadir}/pgsql/extension/redis--0.0.1.sql
%doc %{_datadir}/doc/extension/redis.mmd

%changelog
* Fri Jul  9 2021 root
-
