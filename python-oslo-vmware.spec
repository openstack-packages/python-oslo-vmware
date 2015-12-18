%global pypi_name oslo.vmware
%global pkg_name oslo-vmware

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

Name:           python-%{pkg_name}
Version:        XXX
Release:        XXX
Summary:        Oslo VMware library for OpenStack projects

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%package -n python2-%{pkg_name}
Summary:        Oslo VMware library for OpenStack projects
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr
# test dependencies
BuildRequires: python-fixtures
BuildRequires: python-mock
BuildRequires: python-mox3
BuildRequires: python-subunit
BuildRequires: python-testrepository
BuildRequires: python-testscenarios
BuildRequires: python-testtools
BuildRequires: python-coverage
BuildRequires: python-suds
BuildRequires: python-oslo-utils
BuildRequires: python-oslo-i18n

Requires:  python-stevedore
Requires:  python-netaddr
Requires:  python-iso8601
Requires:  python-six
Requires:  python-babel
Requires:  python-suds
Requires:  python-eventlet
Requires:  PyYAML

%description -n python2-%{pkg_name}
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common VMware library

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx
BuildRequires: python-netaddr
BuildRequires: python-oslo-concurrency
BuildRequires: python-oslo-i18n
BuildRequires: python-oslo-utils
BuildRequires: python-requests >= 2.3.0
BuildRequires: python-suds


%description -n python-%{pkg_name}-doc
Documentation for OpenStack common VMware library.

%package -n python-%{pkg_name}-tests
Summary:    Test subpackage for OpenStack common VMware library

Requires: python-fixtures
Requires: python-mock
Requires: python-mox3
Requires: python-subunit
Requires: python-testrepository
Requires: python-testscenarios
Requires: python-testtools
Requires: python-coverage
Requires: python-suds
Requires: python-oslo-utils
Requires: python-oslo-i18n

%description -n python-%{pkg_name}-tests
Documentation for OpenStack common VMware library.

%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:        Oslo VMware library for OpenStack projects
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# test dependencies
BuildRequires: python3-fixtures
BuildRequires: python3-mock
BuildRequires: python3-mox3
BuildRequires: python3-subunit
BuildRequires: python3-testrepository
BuildRequires: python3-testscenarios
BuildRequires: python3-testtools
BuildRequires: python3-coverage
BuildRequires: python3-suds
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslo-i18n

Requires:  python3-stevedore
Requires:  python3-netaddr
Requires:  python3-iso8601
Requires:  python3-six
Requires:  python3-babel
Requires:  python3-suds
Requires:  python3-eventlet
Requires:  python3-PyYAML

%description -n python3-%{pkg_name}
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.
%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%py2_build

# generate html docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
%{__python2} setup.py build_sphinx

# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif

%files -n python2-%{pkg_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/oslo_vmware
%{python2_sitelib}/*.egg-info
%exclude %{python2_sitelib}/oslo_vmware/tests

%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE

%files -n python-%{pkg_name}-tests
%{python2_sitelib}/oslo_vmware/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_vmware
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_vmware/tests
%endif

%changelog
