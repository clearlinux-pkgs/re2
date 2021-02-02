#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : re2
Version  : 2021.02.02
Release  : 23
URL      : https://github.com/google/re2/archive/2021-02-02/re2-2021.02.02.tar.gz
Source0  : https://github.com/google/re2/archive/2021-02-02/re2-2021.02.02.tar.gz
Summary  : RE2 is a fast, safe, thread-friendly regular expression engine.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: re2-lib = %{version}-%{release}
Requires: re2-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
This is the source code repository for RE2, a regular expression library.
For documentation about how to install and use RE2,
visit https://github.com/google/re2/.

%package dev
Summary: dev components for the re2 package.
Group: Development
Requires: re2-lib = %{version}-%{release}
Provides: re2-devel = %{version}-%{release}
Requires: re2 = %{version}-%{release}

%description dev
dev components for the re2 package.


%package lib
Summary: lib components for the re2 package.
Group: Libraries
Requires: re2-license = %{version}-%{release}

%description lib
lib components for the re2 package.


%package license
Summary: license components for the re2 package.
Group: Default

%description license
license components for the re2 package.


%prep
%setup -q -n re2-2021-02-02
cd %{_builddir}/re2-2021-02-02
pushd ..
cp -a re2-2021-02-02 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612287590
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  includedir=/usr/include libdir=/usr/lib64

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export FFLAGS="$FFLAGS -m64 -march=haswell"
export FCFLAGS="$FCFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
make  %{?_smp_mflags}  includedir=/usr/include libdir=/usr/lib64
popd

%install
export SOURCE_DATE_EPOCH=1612287590
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/re2
cp %{_builddir}/re2-2021-02-02/LICENSE %{buildroot}/usr/share/package-licenses/re2/e310076ee4f65219003bfae2427646e0236c5141
cp %{_builddir}/re2-2021-02-02/re2/fuzzing/compiler-rt/LICENSE %{buildroot}/usr/share/package-licenses/re2/483d1c97dc79ef8741eae507897ca39cfe19da36
pushd ../buildavx2/
%make_install_avx2 includedir=/usr/include libdir=/usr/lib64
popd
%make_install includedir=/usr/include libdir=/usr/lib64

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/re2/filtered_re2.h
/usr/include/re2/re2.h
/usr/include/re2/set.h
/usr/include/re2/stringpiece.h
/usr/lib64/haswell/libre2.so
/usr/lib64/libre2.so
/usr/lib64/pkgconfig/re2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libre2.so.9
/usr/lib64/haswell/libre2.so.9.0.0
/usr/lib64/libre2.so.9
/usr/lib64/libre2.so.9.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/re2/483d1c97dc79ef8741eae507897ca39cfe19da36
/usr/share/package-licenses/re2/e310076ee4f65219003bfae2427646e0236c5141
