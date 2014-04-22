Name: paxctl
Version: 0.7
Release: 1%{?dist}
Summary: Manages various PaX related program header flags for Elf32, Elf64, binaries
Group: Applications/System
License: GPLv2
URL: http://pax.grsecurity.net/
Source0: http://pax.grsecurity.net/paxctl-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: binutils
Requires: binutils

%description

This is paxctl for controlling PaX flags on a per binary basis. PaX is an
intrusion prevention system that provides the best protection mechanisms
against memory corruption bugs. Some applications are not compatible with
certain features (due to design or bad engineering) and therefore they have to
be exempted from certain enforcements. It is also possible to use PaX in soft
mode where none of the protection mechanisms are active by default - here
paxctl can be used to turn them on for selected programs (e.g., network
daemons, programs that process network data such as mail clients, web browsers,
etc).

PaX and paxctl work on ELF executables, both of the standard ET_EXEC and the
newer ET_DYN kind (older PaX releases referred to the latter as ET_DYN
executables, these days they are called Position Independent Executables or
PIEs for short).

%prep
%setup -q
sed "s:--owner 0 --group 0::g" -i Makefile

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin $RPM_BUILD_ROOT/usr/share/man/man1
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/sbin/paxctl
/usr/share/man/man1/paxctl.1.gz

%changelog
* Mon Apr 21 2014 Rudy Grigar <basic@drupal.org> - 0.7-1
- Initial paxctl build
