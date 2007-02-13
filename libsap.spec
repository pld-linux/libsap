Summary:	Emulation library of CPU 6502 and Pokey chip used in Atari XL/XE
Summary(pl.UTF-8):	Biblioteka emulacji procesora 6502 i układu Pokey z Atari XL/XE
Name:		libsap
Version:	1.54.1
Release:	1
License:	Freeware
Group:		Libraries
#Source0:	http://kunik.republika.pl/sap/dl/%{name}-%{version}.tar.gz
Source0:	http://asma.atari.org/bin/sapsrc.zip
# Source0-md5:	11a365228b2a88f6c47174c1c693e04e
Patch0:		%{name}-linux.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-warnings.patch
Patch3:		%{name}-c.patch
URL:		http://kunik.republika.pl/sap/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SAP Library is a software emulation of CPU 6502 microprocessor and
Pokey chip. Those two chips are used in Atari XL/XE computers. SAP
Library is used to to run programs written in 6502 machine language,
programs that are using Pokey chip to play tunes and sounds.

%description -l pl.UTF-8
Biblioteka SAP to programowa emulacja procesora 6502 oraz układu
Pokey. Te dwa układy były używane w komputerach Atari XL/XE.
Biblioteka SAP służy do uruchamiania napisanych w języku maszynowym
6502 programów, które używają układu Pokey do odtwarzania muzyki i
dźwięków.

%package devel
Summary:	Header files for libsap
Summary(pl.UTF-8):	Pliki nagłówkowe libsap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libsap.

%description devel -l pl.UTF-8
Pliki nagłówkowe libsap.

%package static
Summary:	Static libsap library
Summary(pl.UTF-8):	Statyczna biblioteka libsap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsap library.

%description static -l pl.UTF-8
Statyczna biblioteka libsap.

%prep
%setup -q -n sap.src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f sapLib.h libsap.h
ln -sf libsap.h sapLib.h

%build
%{__make} libsap.la \
	CC="%{__cxx}" \
	OPTS="%{rpmcflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README legal.txt pokey.png
%attr(755,root,root) %{_libdir}/libsap.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsap.so
%{_libdir}/libsap.la
%{_includedir}/libsap.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsap.a
