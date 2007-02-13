#
# Conditional build:
%bcond_without	perl		# with perl support
%bcond_without	python		# with python support 
#
Summary:	A MUD client for Unix
Summary(pl.UTF-8):	Klient MUD dla Uniksa
Summary(pt_BR.UTF-8):	Um cliente de MUD para Unix
Name:		mcl
Version:	0.53.00
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://www.andreasen.org/mcl/dist/%{name}-%{version}-src.tar.gz
# Source0-md5:	db67b299d26d8856045df0277078c8ca
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-pic.patch
URL:		http://www.andreasen.org/mcl/
%{?with_perl:BuildRequires:	perl-devel}
%{?with_python:BuildRequires:	python-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcl is a MUD client running under Unix. Under Linux console, it uses
direct Virtual Console access for high speed, but it can also run in
an xterm or on a VT100/ANSI compatible terminal at a reduced speed.
Embedded Perl and Python provide a high degree of tweakability.

%description -l pl.UTF-8
mcl jest klientem MUD działającym pod Uniksem. Na linuksowej konsoli
używa bezpośredniego dostępu do wirtualnej konsoli, aby osiągnąć dużą
szybkość, ale może działać też pod xtermem lub terminalu VT100/ANSI z
ograniczoną prędkością. Wbudowany Perl i Python dają duże możliwości.

%description -l pt_BR.UTF-8
O mcl é um cliente de MUD que roda no Unix. No console virtual do
Linux ele usa acesso direto ao console para obter uma velocidade
maior, mas ele também pode rodar em um xterm, ou em um terminal
compatível com a especificação VT100/ANSI, em uma velocidade inferior.
O mcl tem suporte a scripts via plugins, sendo que já estão
disponíveis perl e python.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	%{!?without_python:--enable-python} \
	%{!?without_perl:--enable-perl}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.1ST doc
%attr(755,root,root) %{_bindir}/mcl
%dir %{_prefix}/lib/mcl
# these seem to be noarch - %{_datadir}/mcl?
%{_prefix}/lib/mcl/auto
%{_prefix}/lib/mcl/contrib
%{_prefix}/lib/mcl/sys
# *.so - %{_libdir}/mcl?
%attr(755,root,root) %{_prefix}/lib/mcl/plugins
