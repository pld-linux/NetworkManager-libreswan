#
# Conditional build:
%bcond_without	gtk4	# Gtk4 version of editor plugin (GNOME 42+)

Summary:	NetworkManager VPN integration for libreswan
Summary(pl.UTF-8):	Integracja NetworkManagera z sieciami VPN opartymi o libreswan
Name:		NetworkManager-libreswan
Version:	1.2.24
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/NetworkManager-libreswan/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	20bad3b0fbce2b5ce6fffec38de3d589
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	gtk+3-devel >= 3.4.0
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.0}
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnl-devel >= 1:3.2.8
%{?with_gtk4:BuildRequires:	libnma-gtk4-devel >= 1.8.33}
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.2.0
Requires:	NetworkManager-gtk-lib >= 1.2.0
Requires:	glib2 >= 1:2.36
Requires:	gtk+3 >= 3.4.0
Requires:	libnl >= 1:3.2.8
Requires:	libsecret >= 0.18
Provides:	NetworkManager-openswan = %{version}-%{release}
Obsoletes:	NetworkManager-openswan < 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libreswan VPN client plugin for NetworkManager.

Support for configuring IKEv1 based IPsec virtual private network
connections. Compatible with Libreswan and Cisco IPsec VPN servers.

%description -l pl.UTF-8
Wtyczka klienta VPN Libreswan dla NetworkManagera. Pozwala na
konfigurowanie wirtualnych sieci prywatnych (VPN) IPsec opartych na
IKEv1, jest zgodna z serwerami VPN Libreswan oraz Cisco IPsec.

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
	--disable-silent-rules \
	--disable-static \
	%{?with_gtk4:--with-gtk4}
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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan-editor.so
%if %{with gtk4}
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-libreswan-editor.so
%endif
%attr(755,root,root) %{_libexecdir}/nm-libreswan-auth-dialog
%attr(755,root,root) %{_libexecdir}/nm-libreswan-service
%attr(755,root,root) %{_libexecdir}/nm-libreswan-service-helper
%{_prefix}/lib/NetworkManager/VPN/nm-libreswan-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-libreswan-service.conf
%{_datadir}/metainfo/network-manager-libreswan.metainfo.xml
%{_mandir}/man5/nm-settings-libreswan.5*
