Summary:	IIO accelerometer sensor to input device proxy
Name:		iio-sensor-proxy
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/hadess/iio-sensor-proxy/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	047659bebd9c071862b0b1fd0be093b5
Patch0:		static-inline.patch
URL:		https://github.com/hadess/iio-sensor-proxy
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	pkg-config
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	udev-glib-devel
Requires(post,preun,postun):	systemd-units >= 38
Requires:	systemd-units >= 0.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IIO accelerometer sensor to input device proxy.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-udevrulesdir=/lib/udev/rules.d \
	--with-systemdsystemunitdir=/lib/systemd/system

%{__make} V=1

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
/etc/dbus-1/system.d/net.hadess.SensorProxy.conf
%{systemdunitdir}/iio-sensor-proxy.service
/lib/udev/rules.d/40-iio-sensor-proxy.rules
%attr(755,root,root) %{_bindir}/monitor-sensor
%attr(755,root,root) %{_sbindir}/iio-sensor-proxy
