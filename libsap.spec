Summary:	Emulation library of CPU 6502 and Pokey chip used in Atari XL/XE
Summary(pl):	Biblioteka emulacji procesora 6502 i uk≥adu Pokey z Atari XL/XE
Name:		libsap
Version:	1.51.1
Release:	2
License:	freeware
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Source0:	http://kunik.republika.pl/sap/dl/%{name}-%{version}.tar.gz
URL:		http://kunik.republika.pl/sap/
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

%prep
%setup -q

%build
%{__make} static \
	CC="%{__cc}" OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install libsap.a $RPM_BUILD_ROOT%{_libdir}
install libsap.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf README LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz pokey.png
%{_libdir}/libsap.a
%{_includedir}/libsap.h
