%define 	module	suds
Summary:	Python SOAP client library
Summary(pl.UTF-8):	Biblioteka klienta SOAP dla języka Python
Name:		python-%{module}
Version:	0.4.1
Release:	1
License:	GPL v3
Group:		Development/Languages/Python
Source0:	https://fedorahosted.org/releases/s/u/suds/%{name}-%{version}.tar.gz
# Source0-md5:	95a2f04378931e973cbb3cca8f8d9765
URL:		https://fedorahosted.org/suds/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PyXML
Requires:	python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Suds is a lightweight SOAP Python client for consuming Web Services.

%description -l pl.UTF-8
Suds to lekka implementacja klienta SOAP dla języka Python.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/suds
%{py_sitescriptdir}/suds/*.py[co]
%dir %{py_sitescriptdir}/suds/transport
%{py_sitescriptdir}/suds/transport/*.py[co]
%dir %{py_sitescriptdir}/suds/xsd
%{py_sitescriptdir}/suds/xsd/*.py[co]
%dir %{py_sitescriptdir}/suds/mx
%{py_sitescriptdir}/suds/mx/*.py[co]
%dir %{py_sitescriptdir}/suds/sax
%{py_sitescriptdir}/suds/sax/*.py[co]
%dir %{py_sitescriptdir}/suds/umx
%{py_sitescriptdir}/suds/umx/*.py[co]
%dir %{py_sitescriptdir}/suds/bindings
%{py_sitescriptdir}/suds/bindings/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/suds-*.egg-info
%endif
