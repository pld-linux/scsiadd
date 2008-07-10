Summary:	SCSI add/remove utility
Summary(pl.UTF-8):	Narzędzia do dodawania/usuwania dysków SCSI
Name:		scsiadd
Version:	1.96
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://llg.cubic.org/tools/%{name}-%{version}.tar.gz
# Source0-md5:	c2d30bc6893852ad2f9dd616cdbee0be
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Add and remove SCSI devices from your Linux system during runtime. No
need to reboot your system, just because you have switched on an
external device.

%description -l pl.UTF-8
To narzędzie umożliwia dodawanie i usuwanie urządzeń SCSI z systemu
linuksowego podczas jego działania. Nie trzeba restartować systemu
tylko z powodu podłączenia jakiegoś urządzenia zewnętrznego.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	CFLAGS="%{rpmcflags} %{rpmldflags}"
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

mv $RPM_BUILD_ROOT%{_sbindir}/scsiadd $RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) /sbin/scsiadd
%{_mandir}/man8/scsiadd.8*
