Summary:	NetworkManager VPN integration for libreswan
Summary(pl.UTF-8):	Integracja NetworkManagera z libreswan
Name:		NetworkManager-libreswan
Version:	1.2.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-libreswan/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	01248eb95a1e1d647057a45aed85a3af
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnl-devel >= 1:3.2.8
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.2.0
Requires:	NetworkManager-gtk-lib >= 1.2.0
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.4.0
Requires:	libnl >= 1:3.2.8
Requires:	libsecret >= 0.18
Provides:	NetworkManager-openswan = %{version}-%{release}
Obsoletes:	NetworkManager-openswan < 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for libreswan.

%description -l pl.UTF-8
Integracja NetworkManagera z libreswan.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-more-warnings \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la

%find_lang NetworkManager-libreswan

%clean
rm -rf $RPM_BUILD_ROOT

%files -f NetworkManager-libreswan.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-libreswan-properties.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan-editor.so
%attr(755,root,root) %{_libdir}/nm-libreswan-auth-dialog
%attr(755,root,root) %{_libdir}/nm-libreswan-service
%attr(755,root,root) %{_libdir}/nm-libreswan-service-helper
%{_prefix}/lib/NetworkManager/VPN/nm-libreswan-service.name
%{_sysconfdir}/NetworkManager/VPN/nm-libreswan-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-libreswan-service.conf
%{_datadir}/appdata/network-manager-libreswan.metainfo.xml
%dir %{_datadir}/gnome-vpn-properties/libreswan
%{_datadir}/gnome-vpn-properties/libreswan/nm-libreswan-dialog.ui
