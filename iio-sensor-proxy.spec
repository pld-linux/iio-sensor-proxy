Summary:	IIO accelerometer sensor to input device proxy
Summary(pl.UTF-8):	Proxy czujnika przyspieszenia IIO do urządzenia wejściowego
Name:		iio-sensor-proxy
Version:	3.0
Release:	1
License:	GPL v3
Group:		Applications/System
#Source0Download: https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/-/tags
Source0:	https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/uploads/de965bcb444552d328255639b241ce73/%{name}-%{version}.tar.xz
# Source0-md5:	77eb3efd950c8eaf4f89c0ce3b2b914c
URL:		https://gitlab.freedesktop.org/hadess/iio-sensor-proxy
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.56
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	libgudev-devel >= 232
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xz
Requires(post,preun,postun):	systemd-units >= 38
Requires:	glib2 >= 1:2.56
Requires:	libgudev >= 232
Requires:	systemd-units >= 0.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IIO accelerometer sensor to input device proxy.

%description -l pl.UTF-8
Proxy czujnika przyspieszenia IIO do urządzenia wejściowego.

%package apidocs
Summary:	DBus API documentation for iio-sensor-proxy service
Summary(pl.UTF-8):	Dokumentacja API DBus usługi iio-sensor-proxy
Group:		Documentation
BuildArch:	noarch

%description apidocs
DBus API documentation for iio-sensor-proxy service.

%description apidocs -l pl.UTF-8
Dokumentacja API DBus usługi iio-sensor-proxy.

%prep
%setup -q

%build
%{__gtkdocize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir} \
	--with-systemdsystemunitdir=%{systemdunitdir} \
	--with-udevrulesdir=/lib/udev/rules.d

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post iio-sensor-proxy.service

%preun
%systemd_preun iio-sensor-proxy.service

%postun
%systemd_reload

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/monitor-sensor
%attr(755,root,root) %{_sbindir}/iio-sensor-proxy
/etc/dbus-1/system.d/net.hadess.SensorProxy.conf
%{systemdunitdir}/iio-sensor-proxy.service
/lib/udev/rules.d/80-iio-sensor-proxy.rules

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/iio-sensor-proxy
