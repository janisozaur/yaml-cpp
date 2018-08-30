%{?mingw_package_header}

%global pkgname yaml-cpp

Name:           mingw-%{pkgname}
Version:        0.6.2
Release:        3%{?dist}
Summary:        A YAML parser and emitter for C++
Group:          Development/Libraries
License:        MIT 
URL:            https://github.com/jbeder/yaml-cpp
Source0:        https://github.com/jbeder/yaml-cpp/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake

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
%mingw_cmake -DYAML_CPP_BUILD_TESTS=OFF -DYAML_CPP_BUILD_TOOLS=OFF
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/yaml-cpp.dll
%{mingw32_libdir}/yaml-cpp.dll.a
%{mingw32_includedir}/yaml-cpp/traits.h
%{mingw32_includedir}/yaml-cpp/mark.h
%{mingw32_includedir}/yaml-cpp/emitterdef.h
%{mingw32_includedir}/yaml-cpp/ostream_wrapper.h
%{mingw32_includedir}/yaml-cpp/node
%{mingw32_includedir}/yaml-cpp/node/parse.h
%{mingw32_includedir}/yaml-cpp/node/convert.h
%{mingw32_includedir}/yaml-cpp/node/iterator.h
%{mingw32_includedir}/yaml-cpp/node/ptr.h
%{mingw32_includedir}/yaml-cpp/node/emit.h
%{mingw32_includedir}/yaml-cpp/node/impl.h
%{mingw32_includedir}/yaml-cpp/node/detail
%{mingw32_includedir}/yaml-cpp/node/detail/iterator_fwd.h
%{mingw32_includedir}/yaml-cpp/node/detail/bool_type.h
%{mingw32_includedir}/yaml-cpp/node/detail/memory.h
%{mingw32_includedir}/yaml-cpp/node/detail/node_iterator.h
%{mingw32_includedir}/yaml-cpp/node/detail/iterator.h
%{mingw32_includedir}/yaml-cpp/node/detail/impl.h
%{mingw32_includedir}/yaml-cpp/node/detail/node.h
%{mingw32_includedir}/yaml-cpp/node/detail/node_data.h
%{mingw32_includedir}/yaml-cpp/node/detail/node_ref.h
%{mingw32_includedir}/yaml-cpp/node/node.h
%{mingw32_includedir}/yaml-cpp/node/type.h
%{mingw32_includedir}/yaml-cpp/emitter.h
%{mingw32_includedir}/yaml-cpp/emitterstyle.h
%{mingw32_includedir}/yaml-cpp/eventhandler.h
%{mingw32_includedir}/yaml-cpp/contrib
%{mingw32_includedir}/yaml-cpp/contrib/graphbuilder.h
%{mingw32_includedir}/yaml-cpp/contrib/anchordict.h
%{mingw32_includedir}/yaml-cpp/noncopyable.h
%{mingw32_includedir}/yaml-cpp/yaml.h
%{mingw32_includedir}/yaml-cpp/exceptions.h
%{mingw32_includedir}/yaml-cpp/dll.h
%{mingw32_includedir}/yaml-cpp/emittermanip.h
%{mingw32_includedir}/yaml-cpp/binary.h
%{mingw32_includedir}/yaml-cpp/emitfromevents.h
%{mingw32_includedir}/yaml-cpp/parser.h
%{mingw32_includedir}/yaml-cpp/stlemitter.h
%{mingw32_includedir}/yaml-cpp/null.h
%{mingw32_includedir}/yaml-cpp/anchor.h
%{mingw32_prefix}/CMake/yaml-cpp-config-version.cmake
%{mingw32_prefix}/CMake/yaml-cpp-config.cmake
%{mingw32_prefix}/CMake/yaml-cpp-targets-release.cmake
%{mingw32_prefix}/CMake/yaml-cpp-targets.cmake

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/yaml-cpp.dll
%{mingw64_libdir}/yaml-cpp.dll.a
%{mingw64_includedir}/yaml-cpp/traits.h
%{mingw64_includedir}/yaml-cpp/mark.h
%{mingw64_includedir}/yaml-cpp/emitterdef.h
%{mingw64_includedir}/yaml-cpp/ostream_wrapper.h
%{mingw64_includedir}/yaml-cpp/node
%{mingw64_includedir}/yaml-cpp/node/parse.h
%{mingw64_includedir}/yaml-cpp/node/convert.h
%{mingw64_includedir}/yaml-cpp/node/iterator.h
%{mingw64_includedir}/yaml-cpp/node/ptr.h
%{mingw64_includedir}/yaml-cpp/node/emit.h
%{mingw64_includedir}/yaml-cpp/node/impl.h
%{mingw64_includedir}/yaml-cpp/node/detail
%{mingw64_includedir}/yaml-cpp/node/detail/iterator_fwd.h
%{mingw64_includedir}/yaml-cpp/node/detail/bool_type.h
%{mingw64_includedir}/yaml-cpp/node/detail/memory.h
%{mingw64_includedir}/yaml-cpp/node/detail/node_iterator.h
%{mingw64_includedir}/yaml-cpp/node/detail/iterator.h
%{mingw64_includedir}/yaml-cpp/node/detail/impl.h
%{mingw64_includedir}/yaml-cpp/node/detail/node.h
%{mingw64_includedir}/yaml-cpp/node/detail/node_data.h
%{mingw64_includedir}/yaml-cpp/node/detail/node_ref.h
%{mingw64_includedir}/yaml-cpp/node/node.h
%{mingw64_includedir}/yaml-cpp/node/type.h
%{mingw64_includedir}/yaml-cpp/emitter.h
%{mingw64_includedir}/yaml-cpp/emitterstyle.h
%{mingw64_includedir}/yaml-cpp/eventhandler.h
%{mingw64_includedir}/yaml-cpp/contrib
%{mingw64_includedir}/yaml-cpp/contrib/graphbuilder.h
%{mingw64_includedir}/yaml-cpp/contrib/anchordict.h
%{mingw64_includedir}/yaml-cpp/noncopyable.h
%{mingw64_includedir}/yaml-cpp/yaml.h
%{mingw64_includedir}/yaml-cpp/exceptions.h
%{mingw64_includedir}/yaml-cpp/dll.h
%{mingw64_includedir}/yaml-cpp/emittermanip.h
%{mingw64_includedir}/yaml-cpp/binary.h
%{mingw64_includedir}/yaml-cpp/emitfromevents.h
%{mingw64_includedir}/yaml-cpp/parser.h
%{mingw64_includedir}/yaml-cpp/stlemitter.h
%{mingw64_includedir}/yaml-cpp/null.h
%{mingw64_includedir}/yaml-cpp/anchor.h
%{mingw64_prefix}/CMake/yaml-cpp-config-version.cmake
%{mingw64_prefix}/CMake/yaml-cpp-config.cmake
%{mingw64_prefix}/CMake/yaml-cpp-targets-release.cmake
%{mingw64_prefix}/CMake/yaml-cpp-targets.cmake

# See https://fedoraproject.org/wiki/Packaging:MinGW

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- initial version
