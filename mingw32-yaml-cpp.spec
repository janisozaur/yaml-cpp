%{?mingw_package_header}

%global pkgname yaml-cpp

Name:           mingw-%{pkgname}
Version:        0.6.1
Release:        3%{?dist}
Summary:        A YAML parser and emitter for C++
Group:          Development/Libraries
License:        MIT 
URL:            https://github.com/jbeder/yaml-cpp
Source0:        https://github.com/jbeder/yaml-cpp/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  perl
BuildRequires:  libzip-tools

BuildRequires:  mingw32-boost
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-zlib >= 1.1.2

BuildRequires:  mingw64-boost
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-zlib >= 1.1.2


%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.


%package -n mingw32-%{pkgname}
Summary:        C library for reading, creating, and modifying zip archives

%description -n mingw32-%{pkgname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.


%package -n mingw64-%{pkgname}
Summary:        C library for reading, creating, and modifying zip archives

%description -n mingw64-%{pkgname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}

# Remove files we don't need
rm -r %{buildroot}%{mingw32_datadir}/*
rm -r %{buildroot}%{mingw64_datadir}/*


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/zipcmp.exe
%{mingw32_bindir}/zipmerge.exe
%{mingw32_bindir}/ziptool.exe
%{mingw32_bindir}/libzip-5.dll
%{mingw32_libdir}/libzip.dll.a
%{mingw32_libdir}/pkgconfig/libzip.pc
%{mingw32_includedir}/zip.h
%{mingw32_includedir}/zipconf.h

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/zipcmp.exe
%{mingw64_bindir}/zipmerge.exe
%{mingw64_bindir}/ziptool.exe
%{mingw64_bindir}/libzip-5.dll
%{mingw64_libdir}/libzip.dll.a
%{mingw64_libdir}/pkgconfig/libzip.pc
%{mingw64_includedir}/zip.h
%{mingw64_includedir}/zipconf.h


%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- initial version
