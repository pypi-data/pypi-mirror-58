# vim:set ft=spec:
#
# -- global settings ----------------------------------------------------------

%global srcname gwpy

Name:           python-%{srcname}
Version:        1.0.1
Release:        1%{?dist}
Summary:        A python package for gravitational-wave astrophysics

License:        GPL-3.0-or-later
URL:            https://gwpy.github.io
Source0:        %pypi_source

BuildArch:      noarch

# SRPM dependencies
BuildRequires:  python-rpm-macros
BuildRequires:  python-srpm-macros

# python2-gwpy
BuildRequires:  python
BuildRequires:  python2-rpm-macros
BuildRequires:  python2-setuptools

# check requirements for python2-gwpy
BuildRequires:  h5py >= 1.3
BuildRequires:  numpy >= 1.7.1
BuildRequires:  python-pathlib
BuildRequires:  python-six >= 1.5
BuildRequires:  python2-astropy >= 1.1.1
BuildRequires:  python2-dateutil
BuildRequires:  python2-dqsegdb2
BuildRequires:  python2-enum34
BuildRequires:  python2-gwdatafind
BuildRequires:  python2-gwosc
BuildRequires:  python2-lal >= 6.14.0
BuildRequires:  python2-ldas-tools-framecpp >= 2.6.0
BuildRequires:  python2-ligo-segments >= 1.0.0
BuildRequires:  python2-matplotlib >= 1.2.0
BuildRequires:  python2-tqdm >= 4.10.0
BuildRequires:  scipy >= 0.12.1

# python3-gwpy
BuildRequires:  epel-rpm-macros
BuildRequires:  python3-rpm-macros
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-setuptools

# check requirements for python3-gwpy
BuildRequires:  python%{python3_pkgversion}-astropy >= 1.1.1
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-dqsegdb2
BuildRequires:  python%{python3_pkgversion}-gwdatafind
BuildRequires:  python%{python3_pkgversion}-gwosc
BuildRequires:  python%{python3_pkgversion}-h5py >= 1.3
BuildRequires:  python%{python3_pkgversion}-lal >= 6.14.0
BuildRequires:  python%{python3_pkgversion}-ldas-tools-framecpp >= 2.6.0
BuildRequires:  python%{python3_pkgversion}-ligo-segments >= 1.0.0
BuildRequires:  python%{python3_pkgversion}-matplotlib >= 1.2.0
BuildRequires:  python%{python3_pkgversion}-numpy >= 1.7.1
BuildRequires:  python%{python3_pkgversion}-scipy >= 0.12.1
BuildRequires:  python%{python3_pkgversion}-six >= 1.5
BuildRequires:  python%{python3_pkgversion}-tqdm >= 4.10.0

# gwpy-plot
BuildRequires: help2man

%description
GWpy is a collaboration-driven Python package providing tools for
studying data from ground-based gravitational-wave detectors.

GWpy provides a user-friendly, intuitive interface to the common
time-domain and frequency-domain data produced by the LIGO and Virgo
observatories and their analyses, with easy-to-follow tutorials at each
step.

<https://gwpy.github.io>

# Release status

[![PyPI version](https://badge.fury.io/py/gwpy.svg)](http://badge.fury.io/py/gwpy)
[![Conda version](https://img.shields.io/conda/vn/conda-forge/gwpy.svg)](https://anaconda.org/conda-forge/gwpy/)

[![DOI](https://zenodo.org/badge/9979119.svg)](https://zenodo.org/badge/latestdoi/9979119)
[![License](https://img.shields.io/pypi/l/gwpy.svg)](https://choosealicense.com/licenses/gpl-3.0/)
![Supported Python versions](https://img.shields.io/pypi/pyversions/gwpy.svg)

# Development status

[![Linux](https://img.shields.io/circleci/project/github/gwpy/gwpy/master.svg?label=Linux)](https://circleci.com/gh/gwpy/gwpy)
[![OSX](https://img.shields.io/travis/gwpy/gwpy/master.svg?label=macOS)](https://travis-ci.com/gwpy/gwpy)
[![Windows](https://img.shields.io/appveyor/ci/gwpy/gwpy/master.svg?label=Windows)](https://ci.appveyor.com/project/gwpy/gwpy/branch/master)
[![codecov](https://codecov.io/gh/gwpy/gwpy/branch/master/graph/badge.svg)](https://codecov.io/gh/gwpy/gwpy)
[![Maintainability](https://api.codeclimate.com/v1/badges/2cf14445b3e070133745/maintainability)](https://codeclimate.com/github/gwpy/gwpy/maintainability)

# Installation

To install, you can do:

```
conda install -c conda-forge gwpy
```

or

```
python -m pip install gwpy
```

You can test your installation, and its version by

```
python -c "import gwpy; print(gwpy.__version__)"
```

# License

GWpy is released under the GNU General Public License v3.0 or later, see [here](https://choosealicense.com/licenses/gpl-3.0/) for a description of this license, or see the [LICENSE](https://github.com/gwpy/gwpy/blob/master/LICENSE) file for the full text.


# -- python2-gwpy -------------------------------------------------------------

%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       h5py >= 1.3
Requires:       numpy >= 1.7.1
Requires:       python
Requires:       python-pathlib
Requires:       python-six >= 1.5
Requires:       python2-astropy >= 1.1.1
Requires:       python2-dateutil
Requires:       python2-dqsegdb2
Requires:       python2-enum34
Requires:       python2-gwdatafind
Requires:       python2-gwosc
Requires:       python2-lal >= 6.14.0
Requires:       python2-ldas-tools-framecpp >= 2.6.0
Requires:       python2-ligo-segments >= 1.0.0
Requires:       python2-matplotlib >= 1.2.0
Requires:       python2-tqdm >= 4.10.0
Requires:       scipy >= 0.12.1
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
GWpy is a collaboration-driven Python package providing tools for
studying data from ground-based gravitational-wave detectors.
This package provides the Python %{python2_version} library.

# -- python3-gwpy -------------------------------------------------------------

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-astropy >= 1.1.1
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-dqsegdb2
Requires:       python%{python3_pkgversion}-gwdatafind
Requires:       python%{python3_pkgversion}-gwosc
Requires:       python%{python3_pkgversion}-h5py >= 1.3
Requires:       python%{python3_pkgversion}-lal >= 6.14.0
Requires:       python%{python3_pkgversion}-ldas-tools-framecpp >= 2.6.0
Requires:       python%{python3_pkgversion}-ligo-segments >= 1.0.0
Requires:       python%{python3_pkgversion}-matplotlib >= 1.2.0
Requires:       python%{python3_pkgversion}-numpy >= 1.7.1
Requires:       python%{python3_pkgversion}-scipy >= 0.12.1
Requires:       python%{python3_pkgversion}-six >= 1.5
Requires:       python%{python3_pkgversion}-tqdm >= 4.10.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
GWpy is a collaboration-driven Python package providing tools for
studying data from ground-based gravitational-wave detectors.
This package provides the Python %{python3_version} library.

# -- gwpy-plot ----------------------------------------------------------------

%package -n gwpy-plot
Summary:       Command-line GWpy plot generator
Requires:      python2-gwpy = %{version}-%{release}
Conflicts:     python2-gwpy < 1.0.0-1

%description -n gwpy-plot
GWpy is a collaboration-driven Python package providing tools for
studying data from ground-based gravitational-wave detectors.
This package provides the command line plotting interface 'gwpy-plot'

# -- build stages -------------------------------------------------------------

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
# install python3 library
%py3_install

# install python2 library (including gwpy-plot entry point)
%py2_install

# install man page for gwpy-plot
mkdir -vp %{buildroot}%{_mandir}/man1
env PYTHONPATH="%{buildroot}%{python2_sitelib}" COLUMNS=1000 \
help2man \
    --name "Command-line GWpy plot generator" \
    --source "Gwpy-%{version}" \
    --version-string %{version} \
    --section 1 --no-info --no-discard-stderr \
    --output %{buildroot}%{_mandir}/man1/gwpy-plot.1 \
    %{buildroot}%{_bindir}/gwpy-plot

%check
# sanity check python2
export PYTHONPATH="${RPM_BUILD_ROOT}%{python2_sitelib}"
%{__python2} -c "import gwpy; print(gwpy.__version__)"
%{__python2} -m gwpy.time --help
${RPM_BUILD_ROOT}%{_bindir}/gwpy-plot --help

# sanity check python3
export PYTHONPATH="${RPM_BUILD_ROOT}%{python3_sitelib}"
%{__python3} -c "import gwpy; print(gwpy.__version__)"
%{__python3} -m gwpy.time --help

# -- files --------------------------------------------------------------------

%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%files -n gwpy-plot
%{_bindir}/gwpy-plot
%{_mandir}/man1/gwpy-plot.1*

# -- changelog ----------------------------------------------------------------

%changelog
* Mon Jan 06 2020 Duncan Macleod <duncan.macleod@ligo.org> - 1.0.1-1
- GWpy-1.0.1

* Tue Oct 29 2019 Duncan Macleod <duncan.macleod@ligo.org> - 1.0.0-1
- GWpy-1.0.0

* Wed Apr 24 2019 Duncan Macleod <duncan.macleod@ligo.org> - 0.15.0-1
- GWpy-0.15.0

* Fri Mar 22 2019 Duncan Macleod <duncan.macleod@ligo.org> - 0.14.2-1
- GWpy-0.14.2

* Wed Mar 13 2019 Duncan Macleod <duncan.macleod@ligo.org> - 0.14.1-1
- GWpy-0.14.1

* Thu Feb 28 2019 Duncan Macleod <duncan.macleod@ligo.org> - 0.14.0-1
- GWpy-0.14.0

* Tue Feb 05 2019 Duncan Macleod <duncan.macleod@ligo.org> - 0.13.1-1
- 0.13.1

* Tue Feb 05 2019 Duncan Macleod <duncan.macleod@ligo.org> - 0.13.0-1
- 0.13.0

* Wed Sep 19 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.12.2-1
- 0.12.2: bug-fix relase for gwpy-0.12

* Wed Sep 19 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.12.1-1
- 0.12.1: bug-fix release for gwpy-0.12

* Thu Aug 16 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.12.0-1
- 0.12.0: development release of GWpy

* Fri Jun 15 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.11.0-1
- 0.11.0: development release of GWpy

* Thu Apr 19 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.10.1-1
- 0.10.1: bug-fix for gwpy-0.10

* Thu Apr 19 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.10.0-1
- 0.10.0: development release of GWpy

* Sat Mar 24 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.9.0-1
- 0.9.0: development release of GWpy

* Mon Feb 19 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.8.1-1
- 0.8.1: bug-fix for gwpy-0.8

* Sun Feb 18 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.8.0-1
- 0.8.0: development release of GWpy

* Thu Jan 25 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.7.5-1
- 0.7.5: packaging bug-fix for gwpy-0.7

* Thu Jan 25 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.7.4-1
- 0.7.4: packaging bug-fix for gwpy-0.7

* Wed Jan 24 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.7.3-1
- 0.7.3: bug fix release for gwpy-0.7

* Wed Jan 24 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.7.2-1
- 0.7.2: bug fix release for gwpy-0.7

* Mon Jan 22 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.7.1-1
- 0.7.1

* Fri Jan 19 2018 Duncan Macleod <duncan.macleod@ligo.org> - 0.7.0-1
- 0.7.0

* Thu Oct 12 2017 Duncan Macleod <duncan.macleod@ligo.org> - 0.6.2-1
- 0.6.2

* Tue Aug 29 2017 Duncan Macleod <duncan.macleod@ligo.org> - 0.6.1-1
- 0.6.1 release

* Fri Aug 18 2017 Duncan Macleod <duncan.macleod@ligo.org> - 0.6-1
- 0.6 release

* Wed May 24 2017 Duncan Macleod <duncan.macleod@ligo.org> - 0.5.2-1
- 0.5.2

