Summary:	Emulation library of CPU 6502 and Pokey chip used in Atari XL/XE
Summary(pl):	Biblioteka emulacji procesora 6502 i uk³adu Pokey z Atari XL/XE
Name:		libsap
Version:	1.51.1
Release:	5
License:	Freeware
Group:		Libraries
Source0:	http://kunik.republika.pl/sap/dl/%{name}-%{version}.tar.gz
# Source0-md5:	d3fd5419ec9665ef9d420b12890458d4
Patch0:		%{name}-shared.patch
URL:		http://kunik.republika.pl/sap/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SAP Library is a software emulation of CPU 6502 microprocessor and
Pokey chip. Those two chips are used in Atari XL/XE computers. SAP
Library is used to to run programs written in 6502 machine language,
programs that are using Pokey chip to play tunes and sounds.

%description -l pl
Biblioteka SAP to programowa emulacja procesora 6502 oraz uk³ado
Pokey. Te dwa uk³ady by³y u¿ywane w komputerach Atari XL/XE.
Biblioteka SAP s³u¿y do uruchamiania napisanych w jêzyku maszynowym
6502 programów, które u¿ywaj± uk³adu Pokey do odtwarzania muzyki i
d¼wiêków.

%package devel
Summary:	Header files for libsap
Summary(pl):	Pliki nag³ówkowe libsap
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libsap.

%description devel -l pl
Pliki nag³ówkowe libsap.

%package static
Summary:	Static libsap library
Summary(pl):	Statyczna biblioteka libsap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libsap library.

%description static -l pl
Statyczna biblioteka libsap.

%prep
%setup -q
%patch -p1

%build
%{__make} libsap.la \
	CC="%{__cxx}" \
	OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README LICENSE pokey.png
%attr(755,root,root) %{_libdir}/libsap.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsap.so
%{_libdir}/libsap.la
%{_includedir}/libsap.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsap.a
