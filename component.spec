#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : component
Version  : 0.0.1
Release  : 6
URL      : http://pypi.debian.net/component/component-0.0.1.zip
Source0  : http://pypi.debian.net/component/component-0.0.1.zip
Summary  : A python library that makes is easy to consume bower components with python.
Group    : Development/Tools
License  : MIT
Requires: component-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the component package.
Group: Default

%description python
python components for the component package.


%prep
%setup -q -n component-0.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503074174
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1503074174
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
