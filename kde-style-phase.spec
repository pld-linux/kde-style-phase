
%define         _name phase

Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Name:		kde-style-%{_name}
Version:	0.4
Release:	1
License:	X11
Group:		Themes
Source0:	http://www.kde-look.org/content/files/11402-%{_name}-%{version}.tar.gz
# Source0-md5:	4e5f5bf08e0b185318e5d2d4df5b1b5b
Source1:	http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	e5c75ce22f1525b13532b519ae88e7a4
Patch0:		%{_name}-unsermake.patch
URL:		http://www.kde-look.org/content/show.php?content=11402
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phase is a widget style for KDE. It is designed to be functional but
not drab, and aesthetic but not distracting.

%description -l pl
phase to styl dla KDE, zaprojektowany tak aby ³±czyæ funkcjonalno¶æ z
estetyk±, nie rozpraszaj±c jednocze¶nie u¿ytkownika.

%prep
%setup -q -n %{_name}-%{version} -a1
%patch0 -p1

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} cvs  -f admin/Makefile.common

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_datadir}/apps/kstyle/themes/*.themerc
