
%define         _name phase

Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Name:		kde-style-%{_name}
Version:	0.2
Release:	1
License:	X11
Group:		Themes
Source0:	http://www.kde-look.org/content/files/11402-%{_name}-%{version}.tar.gz
# Source0-md5:	ae1ed12fe7d80e50edaa251994149511
URL:		http://www.kde-look.org/content/show.php?content=11402
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRequires:	unsermake
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phase is a widget style for KDE. It is designed to be functional but
not drab, and aesthetic but not distracting.

%description -l pl
phase to styl dla KDE, zaprojektowany tak aby ³±czyæ funkcjonalno¶æ z
estetyk±, jednocze¶nie nie rozpraszaj±c u¿ytkownika.

%prep
%setup -q -n %{_name}-%{version}

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
cp -f /usr/share/automake/config.sub admin

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_datadir}/apps/kstyle/themes/*.themerc
