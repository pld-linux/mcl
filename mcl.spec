# This is the spec file for building a RPM of mcl
# Originaly created by Rodrigo Parra Novo

Summary: A MUD client for Unix
Summary(pt_BR): Um cliente de MUD para Unix
Name: mcl
# The below line is automatically updated
Version: 0.52.99
Release: 1
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Packager: Erwin S. Andreasen <erwin@andreasen.org>
URL: http://www.andreasen.org/mcl/
Source: http://www.andreasen.org/dist/mcl-%{version}-src.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-install-root
Prefix: /usr
DocDir: %{prefix}/doc

%description
mcl is a MUD client running under Unix. Under Linux console, it uses direct
Virtual Console access for high speed, but it can also run in an xterm or on
a VT100/ANSI compatible terminal at a reduced speed. Embedded Perl
and Python provide a high degree of tweakability.

%description -l pt_BR
O mcl é um cliente de MUD que roda no Unix. No console virtual do Linux
ele usa acesso direto ao console para obter uma velocidade  maior,  mas
ele também pode rodar em um xterm, ou em um terminal  compatível  com a
especificação VT100/ANSI, em uma velocidade inferior. O mcl tem suporte
a scripts via plugins, sendo que já estão disponíveis perl e python.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="-s"
./configure --prefix=%{prefix} --with-install-root=$RPM_BUILD_ROOT
make
strip mcl o/plugins/*.so || : # Strip may fail in some cases

%install
make install

%files
%defattr (-, root, root)
%doc README.1ST INSTALL doc/
%{prefix}/bin/mcl
%{prefix}/lib/mcl

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 03 1999 Rodrigo Parra Novo <rodarvus@conectiva.com.br>
- Modified the spec file to work with autoconf
- Allowed non-root builds
- Allowed the use of prefixes in the install
- Create mcl.spec directly from mcl.spec.in
- Modified the RPM group mcl belongs to

* Mon Sep 24 1999 Erwin S. Andreasen <erwin@andreasen.org>
- Moved samples to /usr/lib/mcl/, tweaked things.

* Mon Sep 20 1999 Erwin S. Andreasen <erwin@andreasen.org>
- Plugins added

* Fri Mar 12 1999 Erwin S. Andreasen <erwin@andreasen.org>
- Trying to build the 0.50.02 version myself :)

* Tue Feb 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com.br>
- Updated package to version 0.50.01
- Changed version of perl needed to 5.004
- Removed patch to make mcl compile on an alpha

* Mon Feb 15 1999 Rodrigo Parra Novo <rodarvus@conectiva.com.br>
- Updated package to version 0.50.00
- Added requires perl >= 5.00502
- Added patch to make alpha compile again
- Now mcl goes stripped by default

* Wed Dec 30 1998 Rodrigo Parra Novo <rodarvus@conectiva.com.br>
- First build with RPM (version 0.42.05)
- Added pt_BR translations
