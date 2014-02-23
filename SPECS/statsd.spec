%define _destpath /usr/local
%define _statsd %{_destpath}/%{name}-%{version}
Name:           statsd
Version:        0.7.1
Release:        1%{?dist}
Summary:        A network daemon that runs on the Node.js platform.
License:        MIT License
URL:            https://github.com/etsy/statsd
Source0:        https://github.com/etsy/statsd/archive/v0.7.1.tar.gz   
BuildRoot:      %{name}
Requires:       nodejs >= 0.8
Requires:       npm   

%description
A simple, lightweight network daemon to collect metrics over UDP.


%prep
%setup -q %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_destpath}
cp -rp %{_builddir}/%{name}-%{version} %{buildroot}%{_destpath}

%clean
rm -rf %{buildroot}
# doc packaged twice, I am not sure whether they should move to somewhere by writing '%post' or just delete them.
%files
%defattr(-,root,root,-)
%{_destpath}/%{name}-%{version}
%doc %{_statsd}/README.md 
%doc %{_statsd}/Changelog.md 
%doc %{_statsd}/docs
%config %{_statsd}/exampleConfig.js

%changelog
* Wed Feb 12 2014 Fedora Cloud User
* Tue Feb 18 2014 Fedora Wilbeibi
- 
