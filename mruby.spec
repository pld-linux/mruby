Summary:	Lightweight implementation of the Ruby language
Summary(pl.UTF-8):	Lekka implementacja języka Ruby
Name:		mruby
Version:	2.1.2
Release:	1
License:	MIT
Group:		Development/Languages
#Source0Download: https://github.com/mruby/mruby/releases
Source0:	https://github.com/mruby/mruby/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9d94e6de40a63992c143a3554bdaffd6
# debian addon for man pages
Source1:	http://http.debian.net/debian/pool/main/m/mruby/%{name}_%{version}-3.debian.tar.xz
# Source1-md5:	2c4a8ced6d7d863e14d30a27e92188e0
Patch0:		%{name}-optimize.patch
URL:		https://mruby.org/
BuildRequires:	bison
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	ruby >= 1:2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mruby is the lightweight implementation of the Ruby language complying
to (part of) the ISO standard. Its syntax is Ruby 2.x compatible.

This package contains:
- mruby interpreter
- mirb interactive mruby shell
- mrbc compiler

%description -l pl.UTF-8
mruby to lekka implementacja języka Ruby, zgodna z (częścią) standardu
ISO. Składnia jest zgodna z Rubym 2.x.

Ten pakiet zawiera programy:
- interpreter mruby
- interaktywną powłokę mirb
- kompilator mrbc

%package devel
Summary:	Embeddable lightweight implementation of the Ruby language
Summary(pl.UTF-8):	Osadzalna, lekka implementacja języka Ruby
Group:		Development/Libraries

%description devel
mruby is the lightweight implementation of the Ruby language complying
to (part of) the ISO standard. Its syntax is Ruby 2.x compatible.

This package contains embeddable library and its header files.

%description devel -l pl.UTF-8
mruby to lekka implementacja języka Ruby, zgodna z (częścią) standardu
ISO. Składnia jest zgodna z Rubym 2.x.

Ten pakiet zawiera osadzalną bibliotekę oraz jej pliki nagłówkowe.

%prep
%setup -q -a1
%patch -P0 -p1

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -std=gnu99 -fPIC" \
./minirake --verbose

%{?with_tests:./minirake test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}/man1}

cp -p build/host-debug/bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p build/host/bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p build/host/lib/*.a $RPM_BUILD_ROOT%{_libdir}
cp -pr include/* $RPM_BUILD_ROOT%{_includedir}

cp -p debian/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LEGAL LICENSE NEWS README.md TODO
%attr(755,root,root) %{_bindir}/mirb
%attr(755,root,root) %{_bindir}/mrbc
%attr(755,root,root) %{_bindir}/mrdb
%attr(755,root,root) %{_bindir}/mruby
%attr(755,root,root) %{_bindir}/mruby-strip
%{_mandir}/man1/mirb.1*
%{_mandir}/man1/mrbc.1*
%{_mandir}/man1/mrdb.1*
%{_mandir}/man1/mruby.1*
%{_mandir}/man1/mruby-strip.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmruby.a
%{_libdir}/libmruby_core.a
%{_includedir}/mruby
%{_includedir}/mrbconf.h
%{_includedir}/mruby.h
