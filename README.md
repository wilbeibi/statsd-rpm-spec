# Statsd rpm specfile
=========
An [statsd](https://github.com/etsy/statsd) RPM for Fedora

### Steps to install
	
	yum install rpm-build rpmdevtools nodejs npm
	git clone git@github.com:Wilbeibi/statsd-rpm-spec.git
	cd ~/rpmbuild/SPEC
	rpmbuild -ba statsd.spec
	yum localinstall ~/rpmbuild/RPMS/i686/statsd-0.7.1-1.fc20.i686.rpm
	
### What it does
+ Install statsd and related dependencies in /usr/local

### Is it useful
+ I am afraid not. This is just an assignment of [System Administration](https://github.com/jschauma/cs615asa).