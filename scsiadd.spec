Summary:	SCSI add/remove utility
Summary(pl.UTF-8):	Narzędzia do dodawania/usuwania dysków SCSI
Name:		scsiadd
Version:	1.96
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://llg.cubic.org/tools/%{name}-%{version}.tar.gz
# Source0-md5:	c2d30bc6893852ad2f9dd616cdbee0be
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

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
%{__autoconf}
%configure

%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_sbindir}/scsiadd
%{_mandir}/man8/scsiadd.8*
