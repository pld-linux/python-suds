#
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Python 2 SOAP client library
Summary(pl.UTF-8):	Biblioteka klienta SOAP dla Pythona 2
Name:		python-suds
Version:	0.8.4
Release:	7
License:	LGPL v3+
Group:		Development/Languages/Python
#Source0Download: https://github.com/suds-community/suds/releases
Source0:	https://github.com/suds-community/suds/archive/v%{version}/suds-%{version}.tar.gz
# Source0-md5:	d4c47fec087d81f9a02f70bcc48c92c4
Patch0:		%{name}-pytest.patch
URL:		https://github.com/suds-community/suds
BuildRequires:	python-devel >= 1:2.4
%{?with_tests:BuildRequires:	python-pytest}
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Suds is a lightweight SOAP Python client for consuming Web Services.

%description -l pl.UTF-8
Suds to lekka implementacja klienta SOAP dla języka Python.

%prep
%setup -q -n suds-%{version}
%patch -P 0 -p1

%build
topdir=$(pwd)
%py_build

PYTHONPATH=$(pwd)/build-2/lib \
%{__python} -m pytest tests

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md TODO.txt
%{py_sitescriptdir}/suds
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/suds_community-%{version}-py*.egg-info
%endif
