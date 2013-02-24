#
# Conditional build:
%bcond_without	enigmail	# don't build enigmail - GPG/PGP support
%bcond_without	gnomeui		# disable gnomeui support
%bcond_without	gnome		# disable gnomeui (alias)
%bcond_without	ldap		# disable e-mail address lookups in LDAP directories
%bcond_without	lightning	# disable Sunbird/Lightning calendar
%bcond_with	xulrunner	# build with system xulrunner
%bcond_with	tests		# enable tests (whatever they check)
%bcond_without	kerberos	# disable krb5 support

%if %{without gnome}
%undefine	with_gnomeui
%endif

%define		enigmail_ver	1.5.1
%define		nspr_ver	4.9.3
%define		nss_ver		3.14.1
%define		xulrunner_ver	18.0

%if %{without xulrunner}
# The actual sqlite version (see RHBZ#480989):
%define		sqlite_build_version %(pkg-config --silence-errors --modversion sqlite3 2>/dev/null || echo ERROR)
%endif

Summary:	Iceape - web browser
Summary(es.UTF-8):	Navegador de Internet Iceape
Summary(pl.UTF-8):	Iceape - przeglądarka WWW
Summary(pt_BR.UTF-8):	Navegador Iceape
Name:		iceape
Version:	2.15.2
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.bz2
# Source0-md5:	1938c5a9673e94e9f5c809f5dbfe8d29
Source1:	http://www.mozilla-enigmail.org/download/source/enigmail-%{enigmail_ver}.tar.gz
# Source1-md5:	3e71f84ed2c11471282412ebe4f5eb2d
Source2:	%{name}-branding.tar.bz2
# Source2-md5:	0bc28b4382aa8a961f8f7b2ba66d8f89
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
Patch3:		%{name}-glueload-fix.patch
Patch4:		system-mozldap.patch
Patch5:		makefile.patch
Patch6:		system-cairo.patch
# Edit patch below and restore --system-site-packages when system virtualenv gets 1.7 upgrade
Patch7:		system-virtualenv.patch
Patch8:		gyp-slashism.patch
URL:		http://www.pld-linux.org/Packages/Iceape
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.10.2-5
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	freetype-devel >= 1:2.1.8
BuildRequires:	glib2-devel >= 1:2.18
BuildRequires:	gtk+2-devel >= 2:2.10
%{?with_kerberos:BuildRequires:	heimdal-devel >= 0.7.1}
BuildRequires:	hunspell-devel
BuildRequires:	libIDL-devel >= 0.8.0
BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel >= 1.4.7
# standalone libffi 3.0.9 or gcc's from 4.5(?)+
BuildRequires:	libffi-devel >= 6:3.0.9
%{?with_gnomeui:BuildRequires:  libgnome-devel >= 2.0}
%{?with_gnomeui:BuildRequires:  libgnome-keyring-devel}
%{?with_gnomeui:BuildRequires:  libgnomeui-devel >= 2.2.0}
BuildRequires:	libiw-devel
# requires libjpeg-turbo implementing at least libjpeg 6b API
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libnotify-devel >= 0.4
BuildRequires:	libpng(APNG)-devel >= 0.10
BuildRequires:	libpng-devel >= 1.4.1
# rsvg-convert for iceape/branding
BuildRequires:	librsvg
BuildRequires:	libstdc++-devel
BuildRequires:	libvpx-devel >= 1.0.0
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
BuildRequires:	sqlite3-devel >= 3.7.10
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
%if %{with xulrunner}
BuildRequires:	xulrunner-devel >= 2:%{xulrunner_ver}
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
Requires:	gtk+2 >= 2:2.18
Requires:	libjpeg-turbo
Requires:	libpng >= 1.4.1
Requires:	libpng(APNG) >= 0.10
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.14.0
Requires:	sqlite3 >= %{sqlite_build_version}
Requires:	startup-notification >= 0.8
%endif
Provides:	iceape-embedded = %{epoch}:%{version}-%{release}
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

%package addon-enigmail
Summary:	Enigmail %{enigmail_ver} - PGP/GPG support for Iceape
Summary(pl.UTF-8):	Enigmail %{enigmail_ver} - obsługa PGP/GPG dla Iceape
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnupg >= 1.4.2.2
Obsoletes:	seamonkey-addon-enigmail

%description addon-enigmail
Enigmail is an extension to the mail client of Iceape / SeaMonkey /
Mozilla / Netscape and Mozilla Thunderbird which allows users to
access the authentication and encryption features provided by GnuPG.

%description addon-enigmail -l pl.UTF-8
Enigmail jest rozszerzeniem dla klienta pocztowego Iceape, SeaMonkey,
Mozilla i Mozilla Thunderdbird pozwalającym użytkownikowi korzystać z
funkcjonalności GnuPG.

%package chat
Summary:	Iceape Chat - integrated IRC client
Summary(pl.UTF-8):	Iceape Chat - zintegrowany klient IRC-a
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
tar -C mailnews/extensions -zxf %{SOURCE1}
tar -jxf %{SOURCE2}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

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
ac_add_options --disable-elf-hack
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
ac_add_options --enable-gio
%if %{with gnomeui}
ac_add_options --enable-gnomeui
%else
ac_add_options --disable-gnomeui
%endif
ac_add_options --disable-gnomevfs
%if %{with ldap}
ac_add_options --enable-ldap
ac_add_options --with-system-ldap
%else
ac_add_options --disable-ldap
%endif
%if %{with crashreporter}
ac_add_options --enable-crashreporter
%else
ac_add_options --disable-crashreporter
%endif
ac_add_options --disable-xterm-updates
ac_add_options --enable-postscript
%if %{with lightning}
ac_add_options --enable-calendar
%else
ac_add_options --disable-calendar
%endif
ac_add_options --disable-installer
ac_add_options --disable-javaxpcom
ac_add_options --disable-updater
ac_add_options --enable-crypto
ac_add_options --enable-libxul
ac_add_options --enable-pango
ac_add_options --enable-shared-js
ac_add_options --enable-startup-notification
ac_add_options --enable-system-cairo
ac_add_options --enable-system-hunspell
ac_add_options --enable-system-sqlite
ac_add_options --enable-application=suite
ac_add_options --with-distribution-id=org.pld-linux
ac_add_options --with-branding=iceape/branding
%if %{with xulrunner}
ac_add_options --with-system-libxul
ac_add_options --with-libxul-sdk=$(pkg-config --variable=sdkdir libxul)
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
ac_add_options --with-default-mozilla-five-home=%{_libdir}/%{name}
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

%if %{with enigmail}
cd mailnews/extensions/enigmail
./makemake -r -o %{objdir}
%{__make} -C %{objdir}/mailnews/extensions/enigmail \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%{__make} -C %{objdir}/mailnews/extensions/enigmail xpi \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"
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
%{__make} -C suite/installer stage-package \
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
cp -a mozilla/dist/bin/extensions/calendar-timezones@mozilla.org \
	mozilla/dist/bin/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/extensions
		
# move arch independant ones to datadir
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/isp $RPM_BUILD_ROOT%{_datadir}/%{name}/isp
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/modules $RPM_BUILD_ROOT%{_datadir}/%{name}/modules
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
%if %{without xulrunner}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/greprefs.js $RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs.js
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/res $RPM_BUILD_ROOT%{_datadir}/%{name}/res
%endif

ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/isp $RPM_BUILD_ROOT%{_libdir}/%{name}/isp
ln -s ../../share/%{name}/modules $RPM_BUILD_ROOT%{_libdir}/%{name}/modules
ln -s ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins
%if %{without xulrunner}
ln -s ../../share/%{name}/greprefs.js $RPM_BUILD_ROOT%{_libdir}/%{name}/greprefs.js
ln -s ../../share/%{name}/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res
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
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/%{name}/hyphenation
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/hyphenation
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

%if %{with enigmail}
ext_dir=$RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
install -d $ext_dir/{chrome,components,defaults/preferences,modules}
cd mozilla/dist/bin
cp -rfLp chrome/enigmail.jar $ext_dir/chrome
cp -rfLp components/enig* $ext_dir/components
cp -rfLp components/libenigmime.so $ext_dir/components
cp -rfLp defaults/preferences/enigmail.js $ext_dir/defaults/preferences
cp -rfLp modules/{commonFuncs,enigmailCommon,keyManagement,pipeConsole,subprocess}.jsm $ext_dir/modules
cp -rfLp modules/{subprocess_worker_unix,subprocess_worker_win}.js $ext_dir/modules
cd -
cp -p %{topdir}/comm-release/mailnews/extensions/enigmail/package/install.rdf $ext_dir
cp -p %{topdir}/comm-release/mailnews/extensions/enigmail/package/chrome.manifest $ext_dir/chrome.manifest
%endif

# never package these. always remove
# nss
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{freebl3,nss3,nssckbi,nssdbm3,nssutil3,smime3,softokn3,ssl3}.*
# nspr
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{nspr4,plc4,plds4}.so
# mozldap
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{ldap,ldif,prldap,ssldap}60.so
# testpilot quiz
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/distribution/extensions/tbtestpilot@labs.mozilla.com.xpi

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
%attr(755,root,root) %{_libdir}/%{name}/libxpcom.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%endif

%{_libdir}/%{name}/blocklist.xml
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

%{_libdir}/%{name}/components/Aitc.js
%{_libdir}/%{name}/components/AlarmsManager.js
%{_libdir}/%{name}/components/AppsService.js
%{_libdir}/%{name}/components/BrowserElementParent.js
%{_libdir}/%{name}/components/ColorAnalyzer.js
%{_libdir}/%{name}/components/ContactManager.js
%{_libdir}/%{name}/components/FeedConverter.js
%{_libdir}/%{name}/components/FeedWriter.js
%{_libdir}/%{name}/components/messageWakeupService.js
%{_libdir}/%{name}/components/newMailNotificationService.js
%{_libdir}/%{name}/components/nsAbout.js
%{_libdir}/%{name}/components/nsBrowserContentHandler.js
%{_libdir}/%{name}/components/nsComposerCmdLineHandler.js
%{_libdir}/%{name}/components/nsDOMIdentity.js
%{_libdir}/%{name}/components/nsIDService.js
%{_libdir}/%{name}/components/nsSessionStartup.js
%{_libdir}/%{name}/components/nsSessionStore.js
%{_libdir}/%{name}/components/nsSetDefault.js
%{_libdir}/%{name}/components/nsSidebar.js
%{_libdir}/%{name}/components/nsSuiteDownloadManagerUI.js
%{_libdir}/%{name}/components/nsSuiteGlue.js
%{_libdir}/%{name}/components/nsTypeAheadFind.js
%{_libdir}/%{name}/components/nsUrlClassifierHashCompleter.js
%{_libdir}/%{name}/components/nsUrlClassifierLib.js
%{_libdir}/%{name}/components/nsUrlClassifierListManager.js
%{_libdir}/%{name}/components/SettingsManager.js
%{_libdir}/%{name}/components/SiteSpecificUserAgent.js
%{_libdir}/%{name}/components/smileApplication.js
%{_libdir}/%{name}/components/TCPSocket.js
%{_libdir}/%{name}/components/TCPSocketParentIntermediary.js
%{_libdir}/%{name}/components/Weave.js
%{_libdir}/%{name}/components/Webapps.js
%{_libdir}/%{name}/components/WebContentConverter.js

%{_libdir}/%{name}/components/browser.xpt
%{_libdir}/%{name}/components/components.manifest
%{_libdir}/%{name}/components/interfaces.manifest

%attr(755,root,root) %{_libdir}/%{name}/components/libsuite.so

%if %{without xulrunner}
%{_libdir}/%{name}/dependentlibs.list
%{_libdir}/%{name}/platform.ini
%{_libdir}/%{name}/components/ConsoleAPI.js
%{_libdir}/%{name}/components/FeedProcessor.js
%{_libdir}/%{name}/components/GPSDGeolocationProvider.js
%{_libdir}/%{name}/components/NetworkGeolocationProvider.js
%{_libdir}/%{name}/components/PlacesCategoriesStarter.js
%{_libdir}/%{name}/components/TelemetryPing.js
%{_libdir}/%{name}/components/addonManager.js
%{_libdir}/%{name}/components/amContentHandler.js
%{_libdir}/%{name}/components/amWebInstallListener.js
%{_libdir}/%{name}/components/contentAreaDropListener.js
%{_libdir}/%{name}/components/contentSecurityPolicy.js
%{_libdir}/%{name}/components/crypto-SDR.js
%{_libdir}/%{name}/components/jsconsole-clhandler.js
%{_libdir}/%{name}/components/nsBadCertHandler.js
%{_libdir}/%{name}/components/nsBlocklistService.js
%{_libdir}/%{name}/components/nsContentDispatchChooser.js
%{_libdir}/%{name}/components/nsContentPrefService.js
%{_libdir}/%{name}/components/nsDefaultCLH.js
%{_libdir}/%{name}/components/nsFilePicker.js
%{_libdir}/%{name}/components/nsFormAutoComplete.js
%{_libdir}/%{name}/components/nsFormHistory.js
%{_libdir}/%{name}/components/nsHandlerService.js
%{_libdir}/%{name}/components/nsHelperAppDlg.js
%{_libdir}/%{name}/components/nsINIProcessor.js
%{_libdir}/%{name}/components/nsInputListAutoComplete.js
%{_libdir}/%{name}/components/nsLivemarkService.js
%{_libdir}/%{name}/components/nsLoginInfo.js
%{_libdir}/%{name}/components/nsLoginManager.js
%{_libdir}/%{name}/components/nsLoginManagerPrompter.js
%{_libdir}/%{name}/components/nsPlacesAutoComplete.js
%{_libdir}/%{name}/components/nsPlacesExpiration.js
%{_libdir}/%{name}/components/nsPrompter.js
%{_libdir}/%{name}/components/nsSearchService.js
%{_libdir}/%{name}/components/nsSearchSuggestions.js
%{_libdir}/%{name}/components/nsTaggingService.js
%{_libdir}/%{name}/components/nsUpdateTimerManager.js
%{_libdir}/%{name}/components/nsURLFormatter.js
%{_libdir}/%{name}/components/nsWebHandlerApp.js
%{_libdir}/%{name}/components/storage-Legacy.js
%{_libdir}/%{name}/components/storage-mozStorage.js
%{_libdir}/%{name}/components/txEXSLTRegExFunctions.js
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
%{_libdir}/%{name}/modules
%{_libdir}/%{name}/searchplugins
%if %{with xulrunner}
%{_libdir}/%{name}/xulrunner
%else
%{_libdir}/%{name}/dictionaries
%{_libdir}/%{name}/hyphenation
%{_libdir}/%{name}/greprefs.js
%{_libdir}/%{name}/res
%endif

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/chrome
%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/modules
%if %{with enigmail}
%exclude %{_datadir}/%{name}/modules/commonFuncs.jsm
%exclude %{_datadir}/%{name}/modules/enigmailCommon.jsm
%exclude %{_datadir}/%{name}/modules/keyManagement.jsm
%exclude %{_datadir}/%{name}/modules/pipeConsole.jsm
%exclude %{_datadir}/%{name}/modules/subprocess.jsm
%exclude %{_datadir}/%{name}/modules/subprocess_worker_unix.js
%exclude %{_datadir}/%{name}/modules/subprocess_worker_win.js
%endif
%{_datadir}/%{name}/searchplugins
%if %{without xulrunner}
%{_datadir}/%{name}/greprefs.js
%{_datadir}/%{name}/res
%endif

%dir %{_datadir}/%{name}/extensions
%dir %{_libdir}/%{name}/extensions
# the signature of the default theme
%{_libdir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}.xpi
%{_libdir}/%{name}/extensions/modern@themes.mozilla.org.xpi

# files created by iceape -register
%ghost %{_libdir}/%{name}/components/compreg.dat
%ghost %{_libdir}/%{name}/components/xpti.dat

%{_libdir}/%{name}/components/glautocomp.js
%{_libdir}/%{name}/components/jsmimeemitter.js
%{_libdir}/%{name}/components/mail.xpt
%{_libdir}/%{name}/components/mdn-service.js
%{_libdir}/%{name}/components/msgAsyncPrompter.js
%{_libdir}/%{name}/components/newsblog.js
%{_libdir}/%{name}/components/nsAbAutoCompleteMyDomain.js
%{_libdir}/%{name}/components/nsAbAutoCompleteSearch.js
%{_libdir}/%{name}/components/nsAbLDAPAttributeMap.js
%{_libdir}/%{name}/components/nsLDAPProtocolHandler.js
%{_libdir}/%{name}/components/nsMailNewsCommandLineHandler.js
%{_libdir}/%{name}/components/nsMsgTraitService.js
%{_libdir}/%{name}/components/nsSMTPProtocolHandler.js
%{_libdir}/%{name}/components/offlineStartup.js
%{_libdir}/%{name}/components/smime-service.js

%{_libdir}/%{name}/isp
%dir %{_datadir}/%{name}/isp
%{_datadir}/%{name}/isp/Bogofilter.sfd
%{_datadir}/%{name}/isp/DSPAM.sfd
%{_datadir}/%{name}/isp/POPFile.sfd
%{_datadir}/%{name}/isp/SpamAssassin.sfd
%{_datadir}/%{name}/isp/SpamPal.sfd
%{_datadir}/%{name}/isp/movemail.rdf
%{_datadir}/%{name}/isp/rss.rdf

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
%{_libdir}/%{name}/extensions/calendar-timezones@mozilla.org
%endif

%if %{with enigmail}
%files addon-enigmail
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/defaults
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/chrome
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/chrome.manifest
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/install.rdf
%dir %{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/components
%attr(755,root,root) %{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/components/*.so
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/components/*.xpt
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/components/*.js
%dir %{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/modules
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/modules/*.jsm
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/modules/*.js
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
