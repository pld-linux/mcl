#
# Conditional build:
%bcond_without	perl		# with perl support
%bcond_without	python		# with python support 
#
Summary:	A MUD client for Unix
Summary(pl):	Klient MUD dla uniksa
Summary(pt_BR):	Um cliente de MUD para Unix
Name:		mcl
Version:	0.53.00
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://www.andreasen.org/mcl/dist/%{name}-%{version}-src.tar.gz
# Source0-md5:	db67b299d26d8856045df0277078c8ca
Patch0:		%{name}-ncurses.patch
URL:		http://www.andreasen.org/mcl/
%{?with_perl:BuildRequires:   perl-devel}
%{?with_python:BuildRequires:   python-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcl is a MUD client running under Unix. Under Linux console, it uses
direct Virtual Console access for high speed, but it can also run in
an xterm or on a VT100/ANSI compatible terminal at a reduced speed.
Embedded Perl and Python provide a high degree of tweakability.

%description -l pl
mcl jest klientem MUD dzia³aj±cym pod uniksem. Na linuksowej konsoli
u¿ywa bezpo¶redniego dostêpu do wirtualnej konsoli, aby osi±gn±æ du¿±
szybko¶æ, ale mo¿e dzia³aæ te¿ pod xtermem lub terminalu VT100/ANSI z
ograniczon± prêdko¶ci±. Wbudowany Perl i Python daj± du¿e mo¿liwo¶ci.

%description -l pt_BR
O mcl é um cliente de MUD que roda no Unix. No console virtual do
Linux ele usa acesso direto ao console para obter uma velocidade
maior, mas ele também pode rodar em um xterm, ou em um terminal
compatível com a especificação VT100/ANSI, em uma velocidade inferior.
O mcl tem suporte a scripts via plugins, sendo que já estão
disponíveis perl e python.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{!?without_python:--enable-python} \
	%{!?without_perl:--enable-perl}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.1ST doc
%attr(755,root,root) %{_bindir}/mcl
%{_libdir}/mcl

%clean
rm -rf $RPM_BUILD_ROOT
