Summary:	Emulation library of CPU 6502 and Pokey chip used in Atari XL/XE
Summary(pl):	Biblioteka emulacji procesora 6502 i uk≥adu Pokey z Atari XL/XE
Name:		libsap
Version:	1.51.1
Release:	3
License:	freeware
Group:		Libraries
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://kunik.republika.pl/sap/dl/%{name}-%{version}.tar.gz
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
Biblioteka SAP to programowa emulacja procesora 6502 oraz uk≥ado
Pokey. Te dwa uk≥ady by≥y uøywane w komputerach Atari XL/XE.
Biblioteka SAP s≥uøy do uruchamiania napisanych w jÍzyku maszynowym
6502 programÛw, ktÛre uøywaj± uk≥adu Pokey do odtwarzania muzyki i
dºwiÍkÛw.

%package devel
Summary:	Header files for libsap
Summary(pl):	Pliki nag≥Ûwkowe libsap
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files for libsap.

%description devel -l pl
Pliki nag≥Ûwkowe libsap.

%package static
Summary:	Static libsap library
Summary(pl):	Statyczna biblioteka libsap
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
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
	CC="%{__cc}" OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz pokey.png
%attr(755,root,root) %{_libdir}/libsap.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libsap.h
%attr(755,root,root) %{_libdir}/libsap.la
%attr(755,root,root) %{_libdir}/libsap.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libsap.a
