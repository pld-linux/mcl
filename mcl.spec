Summary:	A MUD client for Unix
Summary(pt_BR): Um cliente de MUD para Unix
Name:		mcl
Version:	0.52.99
Release:	1
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	http://www.andreasen.org/mcl/dist/%{name}-%{version}-src.tar.gz
URL:		http://www.andreasen.org/mcl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcl is a MUD client running under Unix. Under Linux console, it uses
direct Virtual Console access for high speed, but it can also run in
an xterm or on a VT100/ANSI compatible terminal at a reduced speed.
Embedded Perl and Python provide a high degree of tweakability.

%description -l pt_BR
O mcl é um cliente de MUD que roda no Unix. No console virtual do
Linux ele usa acesso direto ao console para obter uma velocidade
maior, mas ele também pode rodar em um xterm, ou em um terminal
compatível com a especificação VT100/ANSI, em uma velocidade inferior.
O mcl tem suporte a scripts via plugins, sendo que já estão
disponíveis perl e python.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%files
%defattr(644,root,root,755)
%doc README.1ST INSTALL doc/
%attr(755,root,root) %{_bindir}/mcl
%{_libdir}/mcl

%clean
rm -rf $RPM_BUILD_ROOT
