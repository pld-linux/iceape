#
# Conditional build:
%bcond_with	gtk3		# GTK+ 3.x instead of 2.x
%bcond_without	ldap		# disable e-mail address lookups in LDAP directories
%bcond_without	lightning	# disable Sunbird/Lightning calendar
%bcond_without	kerberos	# disable krb5 support
%bcond_with	xulrunner	# build with system xulrunner
%bcond_with	crashreporter	# report crashes to crash-stats.mozilla.com
%bcond_with	tests		# enable tests (whatever they check)

%define		nspr_ver	4.10.3
%define		nss_ver		3.16
%define		xulrunner_ver	29.0

%if %{without xulrunner}
# The actual sqlite version (see RHBZ#480989):
%define		sqlite_build_version %(pkg-config --silence-errors --modversion sqlite3 2>/dev/null || echo ERROR)
%endif

Summary:	Iceape - web browser
Summary(es.UTF-8):	Navegador de Internet Iceape
Summary(pl.UTF-8):	Iceape - przeglądarka WWW
Summary(pt_BR.UTF-8):	Navegador Iceape
Name:		iceape
Version:	2.26.1
Release:	5
License:	MPL v2.0
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.bz2
# Source0-md5:	4bfa46b370b4d211eef56b90277a9517
Source2:	%{name}-branding.tar.bz2
# Source2-md5:	3feee544ef515f1dbf19b14479916784
Source3:	%{name}-rm_nonfree.sh
Source4:	%{name}.desktop
Source5:	%{name}-composer.desktop
Source6:	%{name}-chat.desktop
Source7:	%{name}-mail.desktop
Source8:	%{name}-venkman.desktop
Source9:	%{name}.sh
Patch0:		%{name}-branding.patch
Patch1:		%{name}-pld-branding.patch
Patch2:		%{name}-agent.patch
Patch3:		enable-addons.patch
Patch4:		system-mozldap.patch
Patch5:		makefile.patch
Patch6:		%{name}-pixman.patch
# Edit patch below and restore --system-site-packages when system virtualenv gets 1.7 upgrade
Patch7:		system-virtualenv.patch
Patch8:		libvpx2.patch
Patch9:		%{name}-system-xulrunner.patch
Patch10:	gcc5.patch
URL:		http://www.pld-linux.org/Packages/Iceape
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.10.2-5
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	freetype-devel >= 1:2.1.8
BuildRequires:	glib2-devel >= 1:2.20
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.18}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
%{?with_kerberos:BuildRequires:	heimdal-devel >= 0.7.1}
BuildRequires:	hunspell-devel
BuildRequires:	libIDL-devel >= 0.8.0
BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel >= 1.4.7
# standalone libffi 3.0.9 or gcc's from 4.5(?)+
BuildRequires:	libffi-devel >= 6:3.0.9
BuildRequires:	libicu-devel >= 50.1
# requires libjpeg-turbo implementing at least libjpeg 6b API
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libnotify-devel >= 0.4
BuildRequires:	libpng(APNG)-devel >= 0.10
BuildRequires:	libpng-devel >= 2:1.6.7
# rsvg-convert for iceape/branding
BuildRequires:	librsvg
BuildRequires:	libstdc++-devel
BuildRequires:	libvpx-devel >= 1.3.0
BuildRequires:	mozldap-devel
BuildRequires:	nspr-devel >= 1:%{nspr_ver}
BuildRequires:	nss-devel >= 1:%{nss_ver}
BuildRequires:	pango-devel >= 1:1.14.0
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	perl-modules >= 5.004
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	python-virtualenv
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.8.2
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
%if %{with xulrunner}
BuildRequires:	xulrunner-devel >= 2:%{xulrunner_ver}
BuildRequires:	xulrunner-devel < 2:30
%endif
BuildRequires:	yasm
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
Requires(post):	mktemp >= 1.5-18
Requires:	desktop-file-utils
Requires:	hicolor-icon-theme
%if %{with xulrunner}
%requires_eq_to	xulrunner xulrunner-devel
%else
Requires:	browser-plugins >= 2.0
Requires:	cairo >= 1.10.2-5
Requires:	dbus-glib >= 0.60
Requires:	glib2 >= 1:2.20
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.18}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	libjpeg-turbo
Requires:	libpng >= 2:1.6.7
Requires:	libpng(APNG) >= 0.10
Requires:	libvpx >= 1.3.0
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.14.0
Requires:	sqlite3 >= %{sqlite_build_version}
Requires:	startup-notification >= 0.8
%endif
Provides:	iceape-embedded = %{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	iceape-mailnews
Obsoletes:	iceape-gnomevfs
Obsoletes:	light
Obsoletes:	mozilla
Obsoletes:	mozilla-gnomevfs
Obsoletes:	seamonkey
Obsoletes:	seamonkey-calendar
Obsoletes:	seamonkey-libs
Obsoletes:	seamonkey-mailnews
Obsoletes:	seamonkey-gnomevfs
Conflicts:	iceape-lang-resources < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		topdir		%{_builddir}/%{name}-%{version}
%define		objdir		%{topdir}/obj-%{_target_cpu}

%define		filterout_cpp	-D_FORTIFY_SOURCE=[0-9]+

# don't satisfy other packages
%define		_noautoprovfiles	%{_libdir}/%{name}
# and as we don't provide them, don't require either
%define		_noautoreq	libmozjs.so libxpcom.so libxul.so libjemalloc.so %{!?with_xulrunner:libmozalloc.so}
%define		_noautoreqdep	libgfxpsshar.so libgkgfx.so libgtkxtbin.so libjsj.so libxpcom_compat.so libxpistub.so

%description
Iceape is an open-source web browser, designed for standards
compliance, performance and portability.

%description -l es.UTF-8
Iceape es un navegador de Internet que se basa en una versión inicial
de Netscape Communicator.

%description -l pl.UTF-8
Iceape jest potężną graficzną przeglądarką WWW, która jest następcą
Mozilli, która następnie była następczynią Netscape Communikatora.

%description -l pt_BR.UTF-8
O Iceape é um web browser baseado numa versão inicial do Netscape
Communicator.

%description -l ru.UTF-8
Iceape - полнофункциональный web-browser с открытыми исходными
текстами, разработанный для максимального соотвествия стандартам,
максмимальной переносимости и скорости работы

%package addon-lightning
Summary:	An integrated calendar for Iceape
Summary(pl.UTF-8):	Zintegrowany kalendarz dla Iceape
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Obsoletes:	seamonkey-addon-lightning

%description addon-lightning
Lightning is an calendar extension to Icedove email client.

%description addon-lightning -l pl.UTF-8
Lightning to rozszerzenie do klienta poczty Icedove dodające
funkcjonalność kalendarza.

%package chat
Summary:	Iceape Chat - integrated IRC client
Summary(pl.UTF-8):	Iceape Chat - zintegrowany klient IRC-a
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-chat
Obsoletes:	seamonkey-chat

%description chat
Iceape Chat - IRC client that is integrated with the Iceape web
browser.

%description chat -l pl.UTF-8
Iceape - klient IRC-a zintegrowany z przeglądarką Iceape.

%package js-debugger
Summary:	JavaScript debugger for use with Iceape
Summary(pl.UTF-8):	Odpluskwiacz JavaScriptu do używania z Iceape
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-js-debugger
Obsoletes:	seamonkey-js-debugger

%description js-debugger
JavaScript debugger for use with Iceape.

%description js-debugger -l pl.UTF-8
Odpluskwiacz JavaScriptu do używania z Iceape.

%package dom-inspector
Summary:	A tool for inspecting the DOM of pages in Iceape
Summary(pl.UTF-8):	Narzędzie do oglądania DOM stron w Iceape
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-dom-inspector
Obsoletes:	seamonkey-dom-inspector

%description dom-inspector
This is a tool that allows you to inspect the DOM for web pages in
Iceape. This is of great use to people who are doing Iceape chrome
development or web page development.

%description dom-inspector -l pl.UTF-8
To narzędzie pozwala na oglądanie DOM dla stron WWW w Iceape. Jest
bardzo przydatne dla ludzi rozwijających chrome w Iceape lub
tworzących strony WWW.

%prep
%setup -qc
cd comm-release
tar -jxf %{SOURCE2}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p2
%patch10 -p2

%build
cd comm-release
%if %{with xulrunner}
if [ "$(grep -E '^[0-9]+\.' mozilla/config/milestone.txt)" != "%{xulrunner_ver}" ]; then
	echo >&2
	echo >&2 "Xulrunner version %{xulrunner_ver} does not match mozilla/config/milestone.txt!"
	echo >&2
	exit 1
fi
%endif

cp -f %{_datadir}/automake/config.* build/autoconf
cp -f %{_datadir}/automake/config.* mozilla/build/autoconf
cp -f %{_datadir}/automake/config.* mozilla/nsprpub/build/autoconf
cp -f %{_datadir}/automake/config.* ldap/sdks/c-sdk/config/autoconf

cat << EOF > .mozconfig
mk_add_options MOZ_OBJDIR=%{objdir}

export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"

%if %{with crashreporter}
export MOZ_DEBUG_SYMBOLS=1
%endif

# Options for 'configure' (same as command-line options).
ac_add_options --prefix=%{_prefix}
ac_add_options --exec-prefix=%{_exec_prefix}
ac_add_options --bindir=%{_bindir}
ac_add_options --sbindir=%{_sbindir}
ac_add_options --sysconfdir=%{_sysconfdir}
ac_add_options --datadir=%{_datadir}
ac_add_options --includedir=%{_includedir}
ac_add_options --libdir=%{_libdir}
ac_add_options --libexecdir=%{_libexecdir}
ac_add_options --localstatedir=%{_localstatedir}
ac_add_options --sharedstatedir=%{_sharedstatedir}
ac_add_options --mandir=%{_mandir}
ac_add_options --infodir=%{_infodir}
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
ac_add_options --enable-crash-on-assert
%else
ac_add_options --disable-debug
ac_add_options --disable-debug-modules
ac_add_options --disable-logging
ac_add_options --enable-optimize="%{rpmcflags} -Os"
%endif
ac_add_options --disable-strip
ac_add_options --disable-strip-libs
%if %{with tests}
ac_add_options --enable-tests
%else
ac_add_options --disable-tests
%endif
%if %{with lightning}
ac_add_options --enable-calendar
%else
ac_add_options --disable-calendar
%endif
%if %{with crashreporter}
ac_add_options --enable-crashreporter
%else
ac_add_options --disable-crashreporter
%endif
ac_add_options --disable-elf-dynstr-gc
ac_add_options --disable-gnomeui
ac_add_options --disable-gnomevfs
ac_add_options --disable-installer
ac_add_options --disable-javaxpcom
ac_add_options --disable-updater
ac_add_options --disable-xterm-updates
ac_add_options --enable-application=suite
ac_add_options --enable-crypto
ac_add_options --enable-default-toolkit=%{?with_gtk3:cairo-gtk3}%{!?with_gtk3:cairo-gtk2}
ac_add_options --enable-gio
%if %{with ldap}
ac_add_options --enable-ldap
ac_add_options --with-system-ldap
%else
ac_add_options --disable-ldap
%endif
ac_add_options --enable-libxul
ac_add_options --enable-pango
ac_add_options --enable-postscript
ac_add_options --enable-shared-js
ac_add_options --enable-startup-notification
ac_add_options --enable-system-cairo
ac_add_options --enable-system-hunspell
ac_add_options --enable-system-sqlite
ac_add_options --with-branding=iceape/branding
ac_add_options --with-default-mozilla-five-home=%{_libdir}/%{name}
ac_add_options --with-distribution-id=org.pld-linux
%if %{with xulrunner}
ac_add_options --with-libxul-sdk=$(pkg-config --variable=sdkdir libxul)
ac_add_options --with-system-libxul
%endif
ac_add_options --with-pthreads
ac_add_options --with-system-bz2
ac_add_options --with-system-ffi
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
EOF

%{__make} -j1 -f client.mk build \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="%{?_smp_mflags}" \
	installdir=%{_libdir}/%{name} \
	XLIBS="-lX11 -lXt" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%if %{with crashreporter}
# create debuginfo for crash-stats.mozilla.com
%{__make} -j1 -C obj-%{_target_cpu} buildsymbols
%endif

%install
rm -rf $RPM_BUILD_ROOT
cd comm-release
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

%browser_plugins_add_browser %{name} -p %{_libdir}/%{name}/plugins

cd %{objdir}
cwd=`pwd`
%{__make} -C suite/installer stage-package \
	LD_LIBRARY_PATH=$cwd/mozilla/dist/lib \
	DESTDIR=$RPM_BUILD_ROOT \
	installdir=%{_libdir}/%{name} \
	PKG_SKIP_STRIP=1

%{__make} -C iceape/branding install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a mozilla/dist/iceape/* $RPM_BUILD_ROOT%{_libdir}/%{name}/

%if %{with xulrunner}
# >= 5.0 seems to require this
ln -s ../xulrunner $RPM_BUILD_ROOT%{_libdir}/%{name}/xulrunner
%endif

# Enable crash reporter for Thunderbird application
%if %{with crashreporter}
%{__sed} -i -e 's/\[Crash Reporter\]/[Crash Reporter]\nEnabled=1/' $RPM_BUILD_ROOT%{_libdir}/%{name}/application.ini

# Add debuginfo for crash-stats.mozilla.com
install -d $RPM_BUILD_ROOT%{_exec_prefix}/lib/debug%{_libdir}/%{name}
cp -a mozilla/dist/%{name}-%{version}.en-US.linux-*.crashreporter-symbols.zip $RPM_BUILD_ROOT%{_prefix}/lib/debug%{_libdir}/%{name}
%endif

# copy manually lightning files, somewhy they are not installed by make
cp -a mozilla/dist/bin/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/extensions

# move arch independant ones to datadir
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins

ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

%if %{without xulrunner}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/isp $RPM_BUILD_ROOT%{_datadir}/%{name}/isp
ln -s ../../share/%{name}/isp $RPM_BUILD_ROOT%{_libdir}/%{name}/isp
%endif

mv $RPM_BUILD_ROOT%{_libdir}/%{name}/distribution/extensions/* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/

# dir for arch independant extensions besides arch dependant extensions
# see mozilla/xpcom/build/nsXULAppAPI.h
# XRE_SYS_LOCAL_EXTENSION_PARENT_DIR and XRE_SYS_SHARE_EXTENSION_PARENT_DIR
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions
 
%if %{without xulrunner}
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
%endif

%{__sed} -e "s|%MOZAPPDIR%|%{_libdir}/%{name}|" \
	 -e "s|%MOZ_APP_DISPLAYNAME%|Iceape|" \
	%{topdir}/comm-release/mozilla/build/unix/mozilla.in > $RPM_BUILD_ROOT%{_libdir}/%{name}/iceape

sed 's,@LIBDIR@,%{_libdir},' %{SOURCE9} > $RPM_BUILD_ROOT%{_bindir}/iceape
chmod a+rx $RPM_BUILD_ROOT%{_bindir}/iceape

install %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
	$RPM_BUILD_ROOT%{_desktopdir}

# files created by iceape -register
touch $RPM_BUILD_ROOT%{_libdir}/%{name}/components/compreg.dat
touch $RPM_BUILD_ROOT%{_libdir}/%{name}/components/xpti.dat

cat << 'EOF' > $RPM_BUILD_ROOT%{_libdir}/%{name}/register
#!/bin/sh
umask 022
rm -f %{_libdir}/%{name}/components/{compreg,xpti}.dat

# it attempts to touch files in $HOME/.mozilla
# beware if you run this with sudo!!!
export HOME=$(mktemp -d)
# also TMPDIR could be pointing to sudo user's homedir
unset TMPDIR TMP || :

%{_libdir}/%{name}/iceape -register

rm -rf $HOME
EOF
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/register

%if %{without xulrunner}
# never package these. always remove
# mozldap
%{__sed} -i '/lib\(ldap\|ldif\|prldap\)60.so/d' $RPM_BUILD_ROOT%{_libdir}/%{name}/dependentlibs.list
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{ldap,ldif,prldap}60.so
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_libdir}/%{name}/register || :
%update_browser_plugins
%update_icon_cache hicolor
%update_desktop_database

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
	%update_icon_cache hicolor
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iceape

# browser plugins v2
%{_browserpluginsconfdir}/browsers.d/%{name}.*
%config(noreplace) %verify(not md5 mtime size) %{_browserpluginsconfdir}/blacklist.d/%{name}.*.blacklist

%dir %{_libdir}/%{name}
%if %{without xulrunner}
%attr(755,root,root) %{_libdir}/%{name}/libmozalloc.so
%attr(755,root,root) %{_libdir}/%{name}/libmozjs.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%endif

%{_libdir}/%{name}/blocklist.xml
%{_libdir}/%{name}/omni.ja
%attr(755,root,root) %{_libdir}/%{name}/register

%if %{with crashreporter}
%{_libdir}/%{name}/crashreporter
%{_libdir}/%{name}/crashreporter-override.ini
%{_libdir}/%{name}/crashreporter.ini
%{_libdir}/%{name}/Throbber-small.gif
%endif

# config?
%{_libdir}/%{name}/application.ini
%{_libdir}/%{name}/chrome.manifest

%dir %{_libdir}/%{name}/components
%{_libdir}/%{name}/components/components.manifest
%attr(755,root,root) %{_libdir}/%{name}/components/libsuite.so

%if %{without xulrunner}
%{_libdir}/%{name}/dependentlibs.list
%{_libdir}/%{name}/platform.ini
%attr(755,root,root) %{_libdir}/%{name}/components/libdbusservice.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmozgnome.so
%attr(755,root,root) %{_libdir}/%{name}/run-mozilla.sh
%attr(755,root,root) %{_libdir}/%{name}/iceape-bin
%attr(755,root,root) %{_libdir}/%{name}/mozilla-xremote-client
%attr(755,root,root) %{_libdir}/%{name}/plugin-container
%endif

%attr(755,root,root) %{_libdir}/%{name}/iceape
%dir %{_libdir}/%{name}/plugins

# symlinks
%{_libdir}/%{name}/chrome
%{_libdir}/%{name}/defaults
%{_libdir}/%{name}/searchplugins
%if %{with xulrunner}
%{_libdir}/%{name}/xulrunner
%else
%{_libdir}/%{name}/dictionaries
%endif

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/chrome
%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/searchplugins

%dir %{_datadir}/%{name}/extensions
%dir %{_libdir}/%{name}/extensions
# the signature of the default theme
%{_libdir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}.xpi
%{_libdir}/%{name}/extensions/modern@themes.mozilla.org.xpi

# files created by iceape -register
%ghost %{_libdir}/%{name}/components/compreg.dat
%ghost %{_libdir}/%{name}/components/xpti.dat

%if %{without xulrunner}
%{_libdir}/%{name}/isp
%dir %{_datadir}/%{name}/isp
%{_datadir}/%{name}/isp/Bogofilter.sfd
%{_datadir}/%{name}/isp/DSPAM.sfd
%{_datadir}/%{name}/isp/POPFile.sfd
%{_datadir}/%{name}/isp/SpamAssassin.sfd
%{_datadir}/%{name}/isp/SpamPal.sfd
%{_datadir}/%{name}/isp/movemail.rdf
%{_datadir}/%{name}/isp/rss.rdf
%endif

%{_iconsdir}/hicolor/*/apps/iceape.png
%{_iconsdir}/hicolor/scalable/apps/iceape.svg
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-composer.desktop
%{_desktopdir}/%{name}-mail.desktop

%if %{with lightning}
%files addon-lightning
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/application.ini
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/chrome
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/chrome.manifest
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/defaults
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/install.rdf
%dir %{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components
%attr(755,root,root) %{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components/*.so
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components/*.js
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components/*.manifest
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components/*.xpt
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/modules
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/calendar-js
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/timezones.sqlite
%endif

%files chat
%defattr(644,root,root,755)
%{_libdir}/%{name}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}.xpi
%{_desktopdir}/%{name}-chat.desktop

%files js-debugger
%defattr(644,root,root,755)
%{_libdir}/%{name}/extensions/{f13b157f-b174-47e7-a34d-4815ddfdfeb8}.xpi
%{_desktopdir}/%{name}-venkman.desktop

%files dom-inspector
%defattr(644,root,root,755)
%{_libdir}/%{name}/extensions/inspector@mozilla.org.xpi
