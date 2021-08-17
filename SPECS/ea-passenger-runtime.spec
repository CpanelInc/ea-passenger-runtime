Summary: EA4 Passenger shared runtime files
Name: ea-passenger-runtime

# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4590 for more details
%define release_prefix 1

Version: 1.0
Release: %{release_prefix}%{?dist}.cpanel
Group: System Environment/Daemons
License: cPanel License
URL: https://go.cpanel.net/ApplicationManager

Source0: passenger.logrotate
Source1: passenger.tmpfiles

AutoReqProv: no

%description
EA4 Passenger shared runtime files

%install

# logrotate
mkdir -p %{buildroot}/var/log/ea-passenger-analytics
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/logrotate.d/ea-passenger

# tmp files
mkdir -p %{buildroot}/var/run/ea-passenger-runtime
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/ea-passenger.conf

# TODO: passenger.<THING>

%files
%dir /var/log/ea-passenger-analytics
%config %{_sysconfdir}/logrotate.d/ea-passenger
%dir /var/run/ea-passenger-runtime
/usr/lib/tmpfiles.d/ea-passenger.conf

%changelog
* Tue Aug 17 2021 Dan Muey <dan@cpanel.net> - 1.0-1
- ZC-9213: Initial version
