#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Library for computing contrast ratios, as required by WCAG 2.0
Summary(pl.UTF-8):	Biblioteka do liczenia współczynników kontrastu zgodnie z WCAG 2.0
Name:		python-wcag_contrast_ratio
Version:	0.9
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/wcag-contrast-ratio/
Source0:	https://files.pythonhosted.org/packages/source/w/wcag-contrast-ratio/wcag-contrast-ratio-%{version}.tar.gz
# Source0-md5:	5ad2879d24d8558e3ac67843091da33b
URL:		https://pypi.org/project/wcag-contrast-ratio/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for computing contrast ratios, as required by WCAG 2.0.

%description -l pl.UTF-8
Biblioteka do liczenia współczynników kontrastu zgodnie z WCAG 2.0.

%package -n python3-wcag_contrast_ratio
Summary:	Library for computing contrast ratios, as required by WCAG 2.0
Summary(pl.UTF-8):	Biblioteka do liczenia współczynników kontrastu zgodnie z WCAG 2.0
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-wcag_contrast_ratio
A library for computing contrast ratios, as required by WCAG 2.0.

%description -n python3-wcag_contrast_ratio -l pl.UTF-8
Biblioteka do liczenia współczynników kontrastu zgodnie z WCAG 2.0.

%prep
%setup -q -n wcag-contrast-ratio-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc README.rst
%{py_sitescriptdir}/wcag_contrast_ratio
%{py_sitescriptdir}/wcag_contrast_ratio-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-wcag_contrast_ratio
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/wcag_contrast_ratio
%{py3_sitescriptdir}/wcag_contrast_ratio-%{version}-py*.egg-info
%endif
