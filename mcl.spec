Summary:	A MUD client for Unix
Summary(pl):	Klient MUD dla uniksa
Summary(pt_BR):	Um cliente de MUD para Unix
Name:		mcl
Version:	0.52.99
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://www.andreasen.org/mcl/dist/%{name}-%{version}-src.tar.gz
URL:		http://www.andreasen.org/mcl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcl is a MUD client running under Unix. Under Linux console, it uses
direct Virtual Console access for high speed, but it can also run in
an xterm or on a VT100/ANSI compatible terminal at a reduced speed.
Embedded Perl and Python provide a high degree of tweakability.

%description -l pl
mcl jest klientem MUD dzia�aj�cym pod uniksem. Na linuksowej konsoli
u�ywa bezpo�redniego dost�pu do wirtualnej konsoli, aby osi�gn�� du��
szybko��, ale mo�e dzia�a� te� pod xtermem lub terminalu VT100/ANSI z
ograniczon� pr�dko�ci�. Wbudowany Perl i Python daj� du�e mo�liwo�ci.

%description -l pt_BR
O mcl � um cliente de MUD que roda no Unix. No console virtual do
Linux ele usa acesso direto ao console para obter uma velocidade
maior, mas ele tamb�m pode rodar em um xterm, ou em um terminal
compat�vel com a especifica��o VT100/ANSI, em uma velocidade inferior.
O mcl tem suporte a scripts via plugins, sendo que j� est�o
dispon�veis perl e python.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

gzip -9nf README.1ST

%files
%defattr(644,root,root,755)
%doc README.1ST.gz doc
%attr(755,root,root) %{_bindir}/mcl
%{_libdir}/mcl

%clean
rm -rf $RPM_BUILD_ROOT
