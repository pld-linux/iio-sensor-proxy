Summary:	IIO accelerometer sensor to input device proxy
Summary(pl.UTF-8):	Proxy czujnika przyspieszenia IIO do urządzenia wejściowego
Name:		iio-sensor-proxy
Version:	3.9
Release:	1
License:	GPL v3
Group:		Applications/System
#Source0Download: https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/-/tags
Source0:	https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/-/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5c031aef70661df21835804d124f0a8f
URL:		https://gitlab.freedesktop.org/hadess/iio-sensor-proxy
BuildRequires:	glib2-devel >= 1:2.76
BuildRequires:	libgudev-devel >= 237
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.91
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel
BuildRequires:	udev-devel
Requires(post,preun,postun):	systemd-units >= 38
Requires:	glib2 >= 1:2.76
Requires:	libgudev >= 237
Requires:	polkit >= 0.91
Requires:	systemd-units >= 0.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IIO accelerometer sensor to input device proxy.

%description -l pl.UTF-8
Proxy czujnika przyspieszenia IIO do urządzenia wejściowego.

%prep
%setup -q

%build
%meson

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%attr(755,root,root) %{_libexecdir}/iio-sensor-proxy
%{_datadir}/dbus-1/system.d/net.hadess.SensorProxy.conf
%{_datadir}/polkit-1/actions/net.hadess.SensorProxy.policy
%{systemdunitdir}/iio-sensor-proxy.service
/lib/udev/rules.d/80-iio-sensor-proxy.rules
