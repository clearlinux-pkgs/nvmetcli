#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0F9E536552045183 (hch@lst.de)
#
Name     : nvmetcli
Version  : 0.7
Release  : 5
URL      : ftp://ftp.infradead.org/pub/nvmetcli/nvmetcli-0.7.tar.gz
Source0  : ftp://ftp.infradead.org/pub/nvmetcli/nvmetcli-0.7.tar.gz
Source99 : ftp://ftp.infradead.org/pub/nvmetcli/nvmetcli-0.7.tar.gz.asc
Summary  : Command line interface for the kernel NVMe nvmet
Group    : Development/Tools
License  : Apache-2.0
Requires: nvmetcli-bin = %{version}-%{release}
Requires: nvmetcli-license = %{version}-%{release}
Requires: nvmetcli-python = %{version}-%{release}
Requires: nvmetcli-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
This package contains the command line interface to the NVMe over Fabrics
nvmet in the Linux kernel.  It allows configuring the nvmet interactively
as well as saving / restoring the configuration to / from a json file.

%package bin
Summary: bin components for the nvmetcli package.
Group: Binaries
Requires: nvmetcli-license = %{version}-%{release}

%description bin
bin components for the nvmetcli package.


%package license
Summary: license components for the nvmetcli package.
Group: Default

%description license
license components for the nvmetcli package.


%package python
Summary: python components for the nvmetcli package.
Group: Default
Requires: nvmetcli-python3 = %{version}-%{release}

%description python
python components for the nvmetcli package.


%package python3
Summary: python3 components for the nvmetcli package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nvmetcli package.


%prep
%setup -q -n nvmetcli-0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559236849
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nvmetcli
cp COPYING %{buildroot}/usr/share/package-licenses/nvmetcli/COPYING
cp debian/copyright %{buildroot}/usr/share/package-licenses/nvmetcli/debian_copyright
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p mv %{buildroot}/usr/bin
mv %{buildroot}/usr/sbin/nvmetcli %{buildroot}/usr/bin/nvmetcli
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nvmetcli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nvmetcli/COPYING
/usr/share/package-licenses/nvmetcli/debian_copyright

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
