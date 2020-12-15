#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : component
Version  : 0.0.1
Release  : 22
URL      : http://pypi.debian.net/component/component-0.0.1.zip
Source0  : http://pypi.debian.net/component/component-0.0.1.zip
Summary  : A python library that makes is easy to consume bower components with python.
Group    : Development/Tools
License  : MIT
Requires: component-python = %{version}-%{release}
Requires: component-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the component package.
Group: Default
Requires: component-python3 = %{version}-%{release}

%description python
python components for the component package.


%package python3
Summary: python3 components for the component package.
Group: Default
Requires: python3-core
Provides: pypi(component)

%description python3
python3 components for the component package.


%prep
%setup -q -n component-0.0.1
cd %{_builddir}/component-0.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603388606
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
