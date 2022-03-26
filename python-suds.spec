#
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 SOAP client library
Summary(pl.UTF-8):	Biblioteka klienta SOAP dla Pythona 2
Name:		python-suds
Version:	0.8.4
Release:	3
License:	LGPL v3+
Group:		Development/Languages/Python
#Source0Download: https://github.com/suds-community/suds/releases
Source0:	https://github.com/suds-community/suds/archive/v%{version}/suds-%{version}.tar.gz
# Source0-md5:	d4c47fec087d81f9a02f70bcc48c92c4
Patch0:		%{name}-pytest.patch
URL:		https://github.com/suds-community/suds
%if %{with python2}
BuildRequires:	python-devel >= 1:2.4
%{?with_tests:BuildRequires:	python-pytest}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
%{?with_tests:BuildRequires:	python3-pytest}
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Suds is a lightweight SOAP Python client for consuming Web Services.

%description -l pl.UTF-8
Suds to lekka implementacja klienta SOAP dla języka Python.

%package -n python3-suds
Summary:	Python 3 SOAP client library
Summary(pl.UTF-8):	Biblioteka klienta SOAP dla Pythona 3
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-suds
Suds is a lightweight SOAP Python client for consuming Web Services.

%description -n python3-suds -l pl.UTF-8
Suds to lekka implementacja klienta SOAP dla języka Python.

%prep
%setup -q -n suds-%{version}
%patch0 -p1

%build
topdir=$(pwd)
%if %{with python2}
%py_build

PYTHONPATH=$(pwd)/build-2/lib \
%{__python} -m pytest tests
%endif

%if %{with python3}
%py3_build

# python2 version of suds (before 2to3) must not be in cwd when running python3 tests
cd build-3
PYTHONPATH=$(pwd)/lib \
%{__python3} -m pytest ../tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md TODO.txt
%{py_sitescriptdir}/suds
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/suds_community-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-suds
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md TODO.txt
%{py3_sitescriptdir}/suds
%{py3_sitescriptdir}/suds_community-%{version}-py*.egg-info
%endif
