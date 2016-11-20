%global libname xcb-xrm

Name:           xcb-util-xrm
Version:        1.0
Release:        1%{?dist}
Summary:        XCB utility functions for the X resource manager

License:        MIT
URL:            https://github.com/Airblader/xcb-util-xrm
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(x11)

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
autoreconf -vfi
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/lib%{libname}.la

%check
make %{?_smp_mflags} check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/lib%{libname}.so.*

%files devel
%{_includedir}/xcb/%(n=%{libname}; echo ${n//-/_}).h
%{_libdir}/lib%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
* Fri Aug 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0-1
- Initial package
