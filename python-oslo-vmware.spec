%global pypi_name oslo.vmware

Name:           python-oslo-vmware
Version:        XXX
Release:        XXX{?dist}
Summary:        Oslo VMware library for OpenStack projects

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr

Requires:  python-stevedore
Requires:  python-netaddr
Requires:  python-iso8601
Requires:  python-six
Requires:  python-babel
Requires:  python-suds
Requires:  python-eventlet
Requires:  PyYAML

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%package doc
Summary:    Documentation for OpenStack common VMware library
Group:      Documentation

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx

%description doc
Documentation for OpenStack common VMware library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{__python2} setup.py build

# generate html docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
%{__python2} setup.py build_sphinx

# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{python2_sitelib}/oslo
%{python2_sitelib}/oslo_vmware
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/*-nspkg.pth

%files doc
%doc doc/build/html

%changelog
