# TODO:
# - rebranding to iceape is not complete
# - some patches still needs to be reviewed
# - check if any and which files should be moved to mailnews
# - review %files
# - does chatzilla / dom-inspector / venkman need .desktop files?
# - it seems like some gnomeui files are being build no matter
#   if its enabled or disabled
# - svg bcond seems obsolete
# - probably lots and lots of other things
# - application segfaults on statrup
#
# Conditional build:
%bcond_without	gnomevfs	# disable GnomeVFS support
%bcond_with	gnomeui		# enable GnomeUI
%bcond_without	gnome		# disable gnomevfs (alias)
%bcond_without	svg		# disable svg support
#
%if %{without gnome}
%undefine	with_gnomevfs
%endif
%define	enigmail_ver	1.0.1
Summary:	Iceape - web browser
Summary(es.UTF-8):	Navegador de Internet Iceape
Summary(pl.UTF-8):	Iceape - przeglądarka WWW
Summary(pt_BR.UTF-8):	Navegador Iceape
Name:		iceape
Version:	2.0.4
Release:	0.2
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	ftp://ftp.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.bz2
# Source0-md5:	1a7f94a46890a60e0fb3340e567000c0
Source1:	http://www.mozilla-enigmail.org/download/source/enigmail-%{enigmail_ver}.tar.gz
# Source1-md5:	508ca9ab0396afb49e82eda88014924b
Source2:	%{name}-branding.tar.bz2
# Source2-md5:	9707f1671625ac10cb4e52f0033d8776
Source3:	%{name}-rm_nonfree.sh
Source4:	%{name}.desktop
Source5:	%{name}-composer.desktop
Source6:	%{name}-chat.desktop
Source7:	%{name}-mail.desktop
Source8:	%{name}-venkman.desktop
Patch0:		%{name}-branding.patch
Patch1:		%{name}-ldap-with-nss.patch
Patch2:		%{name}-kill_slim_hidden_def.patch
Patch3:		%{name}-lib_path.patch
Patch4:		%{name}-fonts.patch
Patch5:		%{name}-ti-agent.patch
Patch6:		%{name}-agent.patch
Patch7:		%{name}-prefs.patch
Patch8:		%{name}-lcrmf.patch
Patch10:	%{name}-install.patch
URL:		http://www.pld-linux.org/Packages/Iceape
BuildRequires:	automake
BuildRequires:	alsa-lib-devel
%{?with_svg:BuildRequires:	cairo-devel >= 1.0.0}
BuildRequires:	freetype-devel >= 1:2.1.8
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.0.0}
BuildRequires:	gtk+2-devel
BuildRequires:	libIDL-devel >= 0.8.0
%{?with_gnomeui:BuildRequires:	libgnomeui-devel >= 2.0}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.7
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.8
BuildRequires:	nss-devel >= 1:3.12.3
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	pkgconfig
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.356
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.1
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zip >= 2.1
BuildRequires:	zlib-devel >= 1.2.3
Requires:	browser-plugins >= 2.0
%{?with_svg:Requires:	cairo >= 1.0.0}
Requires:	nspr >= 1:4.8
Requires:	nss >= 1:3.12.3
Provides:	iceape-embedded = %{epoch}:%{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	light
Obsoletes:	mozilla
Obsoletes:	seamonkey
Obsoletes:	seamonkey-calendar
Obsoletes:	seamonkey-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_iceapedir	%{_libdir}/%{name}
%define		_chromedir	%{_libdir}/%{name}/chrome

%define		filterout_cpp	-D_FORTIFY_SOURCE=[0-9]+

# iceweasel/icedove/iceape provide their own versions
%define		_noautoreqdep	libgfxpsshar.so libgkgfx.so libgtkxtbin.so libjsj.so libxlibrgb.so libxpcom_compat.so libxpcom_core.so libxpistub.so
# we don't want these to satisfy xulrunner-devel
%define		_noautoprov	libgtkembedmoz.so libldap50.so libmozjs.so libprldap50.so libssldap50.so libxpcom.so libxul.so
# and as we don't provide them, don't require either
%define		_noautoreq	libgtkembedmoz.so libldap50.so libmozjs.so libprldap50.so libssldap50.so libxpcom.so libxul.so

%define		specflags	-fno-strict-aliasing

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

%package mailnews
Summary:	Iceape - programs for mail and news
Summary(pl.UTF-8):	Iceape - programy do poczty i newsów
Summary(ru.UTF-8):	Почтовая система на основе Iceape
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-mailnews
Obsoletes:	seamonkey-mailnews

%description mailnews
Programs for mail and news integrated with browser.

%description mailnews -l pl.UTF-8
Programy pocztowe i obsługa newsów zintegrowane z przeglądarką.

%description mailnews -l ru.UTF-8
Клиент почты и новостей, на основе Iceape Поддерживает IMAP, POP и
NNTP и имеет простой интерфейс пользователя.

%package addon-enigmail
Summary:	Enigmail %{enigmail_ver} - PGP/GPG support for Iceape
Summary(pl.UTF-8):	Enigmail %{enigmail_ver} - obsługa PGP/GPG dla Iceape
Group:		X11/Applications/Networking
Requires(post,postun):	%{name}-mailnews = %{epoch}:%{version}-%{release}
Requires:	%{name}-mailnews = %{epoch}:%{version}-%{release}
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

%package gnomevfs
Summary:	Gnome-VFS module providing support for smb:// URLs
Summary(pl.UTF-8):	Moduł Gnome-VFS dodający wsparcie dla URLi smb://
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-gnomevfs
Obsoletes:	seamonkey-gnomevfs

%description gnomevfs
Gnome-VFS module providing support for smb:// URLs.

%description gnomevfs -l pl.UTF-8
Moduł Gnome-VFS dodający wsparcie dla URLi smb://.

%prep
%setup -qc
mv -f comm-1.9.1 mozilla
cd mozilla
/bin/sh %{SOURCE3}
tar -jxf %{SOURCE2}
tar -C mailnews/extensions -zxf %{SOURCE1}
%patch0 -p1
%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
%if "%{pld_release}" == "ti"
%patch5 -p1
%else
%patch6 -p1
%endif
%patch7 -p1
%patch8 -p1
%patch10 -p1

%build
cd mozilla

cp -f /usr/share/automake/config.* mozilla/build/autoconf
cp -f /usr/share/automake/config.* mozilla/nsprpub/build/autoconf
cp -f /usr/share/automake/config.* directory/c-sdk/config/autoconf
ac_cv_visibility_pragma=no; export ac_cv_visibility_pragma

cat << 'EOF' > .mozconfig
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-%{_target_cpu}

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
%if %{with tests}
ac_add_options --enable-tests
%else
ac_add_options --disable-tests
%endif
%if %{with gnomeui}
ac_add_options --enable-gnomeui
%else
ac_add_options --disable-gnomeui
%endif
%if %{with gnomevfs}
ac_add_options --enable-gnomevfs
%else
ac_add_options --disable-gnomevfs
%endif
ac_add_options --disable-elf-dynstr-gc
ac_add_options --disable-crashreporter
ac_add_options --disable-installer
ac_add_options --disable-pedantic
ac_add_options --disable-strip
ac_add_options --disable-updater
ac_add_options --disable-xterm-updates
ac_add_options --enable-application=suite
ac_add_options --enable-crypto
ac_add_options --enable-default-toolkit=cairo-gtk2
ac_add_options --enable-ldap
ac_add_options --enable-optimize="%{rpmcflags}"
ac_add_options --enable-postscript
ac_add_options --enable-old-abi-compat-wrappers
ac_add_options --enable-startup-notification
ac_add_options --enable-system-cairo
ac_add_options --enable-system-sqlite
ac_add_options --with-default-mozilla-five-home=%{_iceapedir}
ac_add_options --with-pthreads
ac_add_options --with-system-jpeg
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
ac_add_options --with-x
EOF
#ac_add_options --with-branding=iceweasel/branding

%{__make} -j1 -f client.mk build \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

cd mailnews/extensions/enigmail
./makemake -r
cd ../../..
%{__make} -C obj-%{_target_cpu}/mailnews/extensions/enigmail -j1 \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
cd mozilla
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_datadir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} -C obj-%{_target_cpu}/suite/installer stage-package \
	DESTDIR=$RPM_BUILD_ROOT \
	MOZ_PKG_DIR=%{_iceapedir} \
	PKG_SKIP_STRIP=1

# enigmail must be installed manually
install obj-%{_target_cpu}/mozilla/dist/bin/components/{{libenigmime,libipc}.so,{enigmail,enigprefs-service,enigMsgCompFields}.js} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/components
install obj-%{_target_cpu}/mozilla/dist/bin/chrome/{en-US,enigmail,enigmime}.jar \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/chrome

# move arch independant ones to datadir
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/modules $RPM_BUILD_ROOT%{_datadir}/%{name}/modules
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/greprefs $RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/res $RPM_BUILD_ROOT%{_datadir}/%{name}/res

ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/extensions $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions
ln -s ../../share/%{name}/modules $RPM_BUILD_ROOT%{_libdir}/%{name}/modules
ln -s ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins
ln -s ../../share/%{name}/greprefs $RPM_BUILD_ROOT%{_libdir}/%{name}/greprefs
ln -s ../../share/%{name}/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries

touch $RPM_BUILD_ROOT%{_libdir}/%{name}/components/compreg.dat
touch $RPM_BUILD_ROOT%{_libdir}/%{name}/components/xpti.dat

install %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
	$RPM_BUILD_ROOT%{_desktopdir}

install suite/branding/icons/gtk/iceape.png $RPM_BUILD_ROOT%{_pixmapsdir}

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/iceape
#!/bin/sh
# (c) vip at linux.pl, wolf at pld-linux.org

LD_LIBRARY_PATH=%{_iceapedir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH

MOZILLA_FIVE_HOME="%{_iceapedir}"
ICEAPE="$MOZILLA_FIVE_HOME/iceape-bin"
if [ "$1" == "-remote" ]; then
	exec $ICEAPE "$@"
fi

PING=`$ICEAPE -remote 'ping()' 2>&1 >/dev/null`
if [ -n "$PING" ]; then
	if [ -f "`pwd`/$1" ]; then
		exec $ICEAPE "file://`pwd`/$1"
	else
		exec $ICEAPE "$@"
	fi
fi

if [ -z "$1" ]; then
	exec $ICEAPE -remote 'xfeDoCommand (openBrowser)'
elif [ "$1" == "-mail" ]; then
	exec $ICEAPE -remote 'xfeDoCommand (openInbox)'
elif [ "$1" == "-compose" ]; then
	exec $ICEAPE -remote 'xfeDoCommand (composeMessage)'
fi

[[ $1 == -* ]] && exec $ICEAPE "$@"

if [ -f "`pwd`/$1" ]; then
	URL="file://`pwd`/$1"
else
	URL="$1"
fi
if grep -q -E 'browser.tabs.opentabfor.middleclick.*true' \
		~/.mozilla/default/*/prefs.js; then
	exec $ICEAPE -remote "OpenUrl($URL,new-tab)"
				else
	exec $ICEAPE -remote "OpenUrl($URL,new-window)"
fi

echo "Cannot execute Iceape ($ICEAPE)!" >&2
exit 1
EOF

ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/seamonkey

cat << 'EOF' > $RPM_BUILD_ROOT%{_sbindir}/%{name}-chrome+xpcom-generate
#!/bin/sh
umask 022
cd %{_datadir}/%{name}/chrome
cat *-installed-chrome.txt > installed-chrome.txt
rm -f chrome.rdf overlays.rdf
rm -f %{_iceapedir}/components/{compreg,xpti}.dat

LD_LIBRARY_PATH=%{_iceapedir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH

%{_libdir}/%{name}/iceape -register
exit 0
EOF

%browser_plugins_add_browser %{name} -p %{_libdir}/%{name}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/%{name}-chrome+xpcom-generate
%update_browser_plugins

%postun
%{_sbindir}/%{name}-chrome+xpcom-generate
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%post mailnews -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun mailnews -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post addon-enigmail -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun addon-enigmail -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post chat -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun chat -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post js-debugger -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun js-debugger -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post dom-inspector -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun dom-inspector -p %{_sbindir}/%{name}-chrome+xpcom-generate

%post gnomevfs -p %{_sbindir}/%{name}-chrome+xpcom-generate
%postun gnomevfs -p %{_sbindir}/%{name}-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iceape
%attr(755,root,root) %{_bindir}/seamonkey
%attr(744,root,root) %{_sbindir}/%{name}-chrome+xpcom-generate

# browser plugins v2
%{_browserpluginsconfdir}/browsers.d/%{name}.*
%config(noreplace) %verify(not md5 mtime size) %{_browserpluginsconfdir}/blacklist.d/%{name}.*.blacklist

%dir %{_chromedir}
%dir %{_iceapedir}
%dir %{_iceapedir}/components
%dir %{_iceapedir}/defaults
%dir %{_iceapedir}/dictionaries
%dir %{_iceapedir}/extensions
%dir %{_iceapedir}/greprefs
%dir %{_iceapedir}/modules
%dir %{_iceapedir}/plugins
%dir %{_iceapedir}/res
%dir %{_iceapedir}/searchplugins
%dir %{_datadir}/%{name}

%{_iceapedir}/*.ini
%{_iceapedir}/*.xml

%attr(755,root,root) %{_iceapedir}/libxpcom.so
%attr(755,root,root) %{_iceapedir}/libxpcom_core.so
%attr(755,root,root) %{_iceapedir}/libgfxpsshar.so
%attr(755,root,root) %{_iceapedir}/libgkgfx.so
%attr(755,root,root) %{_iceapedir}/libgtkxtbin.so
%attr(755,root,root) %{_iceapedir}/libjsj.so
%attr(755,root,root) %{_iceapedir}/libldap60.so
%attr(755,root,root) %{_iceapedir}/libldif60.so
%attr(755,root,root) %{_iceapedir}/libmozjs.so
%attr(755,root,root) %{_iceapedir}/libprldap60.so
%attr(755,root,root) %{_iceapedir}/libthebes.so
%attr(755,root,root) %{_iceapedir}/libxul.so

%attr(755,root,root) %{_iceapedir}/iceape
%attr(755,root,root) %{_iceapedir}/run-mozilla.sh
%attr(755,root,root) %{_iceapedir}/iceape-bin
%attr(755,root,root) %{_iceapedir}/mozilla-xremote-client

%attr(755,root,root) %{_iceapedir}/components/libaccess*.so
%attr(755,root,root) %{_iceapedir}/components/libappcomps.so
%attr(755,root,root) %{_iceapedir}/components/libauth*.so
%attr(755,root,root) %{_iceapedir}/components/libautoconfig.so
%attr(755,root,root) %{_iceapedir}/components/libcaps.so
%attr(755,root,root) %{_iceapedir}/components/libchardet.so
%attr(755,root,root) %{_iceapedir}/components/libchrome.so
%attr(755,root,root) %{_iceapedir}/components/libcommandlines.so
%attr(755,root,root) %{_iceapedir}/components/libcomposer.so
%attr(755,root,root) %{_iceapedir}/components/libcookie.so
%attr(755,root,root) %{_iceapedir}/components/libdbusservice.so
%attr(755,root,root) %{_iceapedir}/components/libdocshell.so
%attr(755,root,root) %{_iceapedir}/components/libembedcomponents.so
%attr(755,root,root) %{_iceapedir}/components/libfileview.so
%attr(755,root,root) %{_iceapedir}/components/libgk*.so
%attr(755,root,root) %{_iceapedir}/components/libhtmlpars.so
%attr(755,root,root) %{_iceapedir}/components/libi18n.so
%attr(755,root,root) %{_iceapedir}/components/libimg*.so
%attr(755,root,root) %{_iceapedir}/components/libintlapp.so
%attr(755,root,root) %{_iceapedir}/components/libjar50.so
%attr(755,root,root) %{_iceapedir}/components/libjsd.so
%attr(755,root,root) %{_iceapedir}/components/libmork.so
%attr(755,root,root) %{_iceapedir}/components/libmoz*.so
%attr(755,root,root) %{_iceapedir}/components/libnecko*.so
%attr(755,root,root) %{_iceapedir}/components/libns*.so
%attr(755,root,root) %{_iceapedir}/components/liboji.so
%attr(755,root,root) %{_iceapedir}/components/libpermissions.so
%attr(755,root,root) %{_iceapedir}/components/libpipboot.so
%attr(755,root,root) %{_iceapedir}/components/libpipnss.so
%attr(755,root,root) %{_iceapedir}/components/libpippki.so
%attr(755,root,root) %{_iceapedir}/components/libplaces.so
%attr(755,root,root) %{_iceapedir}/components/libpref.so
%attr(755,root,root) %{_iceapedir}/components/librdf.so
%attr(755,root,root) %{_iceapedir}/components/libremoteservice.so
%attr(755,root,root) %{_iceapedir}/components/libsatchel.so
%attr(755,root,root) %{_iceapedir}/components/libspellchecker.so
%attr(755,root,root) %{_iceapedir}/components/libsuite.so
%attr(755,root,root) %{_iceapedir}/components/libstoragecomps.so
%attr(755,root,root) %{_iceapedir}/components/libsystem-pref.so
%attr(755,root,root) %{_iceapedir}/components/libtkautocomplete.so
%attr(755,root,root) %{_iceapedir}/components/libtoolkitcomps.so
%attr(755,root,root) %{_iceapedir}/components/libtxmgr.so
%attr(755,root,root) %{_iceapedir}/components/libuconv.so
%attr(755,root,root) %{_iceapedir}/components/libucv*.so
%attr(755,root,root) %{_iceapedir}/components/libuniversalchardet.so
%attr(755,root,root) %{_iceapedir}/components/libunixproxy.so
%attr(755,root,root) %{_iceapedir}/components/libwebbrwsr.so
%attr(755,root,root) %{_iceapedir}/components/libwidget_gtk2.so
%attr(755,root,root) %{_iceapedir}/components/libwindowds.so
%attr(755,root,root) %{_iceapedir}/components/libx*.so
%attr(755,root,root) %{_iceapedir}/components/libzipwriter.so

%{_iceapedir}/components/browser.xpt

%{_iceapedir}/components/FeedConverter.js
%{_iceapedir}/components/FeedProcessor.js
%{_iceapedir}/components/FeedWriter.js
%{_iceapedir}/components/jsconsole-clhandler.js
%{_iceapedir}/components/NetworkGeolocationProvider.js
%{_iceapedir}/components/nsAboutAbout.js
%{_iceapedir}/components/nsAboutCertError.js
%{_iceapedir}/components/nsAboutFeeds.js
%{_iceapedir}/components/nsAboutRights.js
%{_iceapedir}/components/nsAboutSessionRestore.js
%{_iceapedir}/components/nsAddonRepository.js
%{_iceapedir}/components/nsBadCertHandler.js
%{_iceapedir}/components/nsBlocklistService.js
%{_iceapedir}/components/nsBrowserContentHandler.js
%{_iceapedir}/components/nsComposerCmdLineHandler.js
%{_iceapedir}/components/nsContentDispatchChooser.js
%{_iceapedir}/components/nsContentPrefService.js
%{_iceapedir}/components/nsDefaultCLH.js
%{_iceapedir}/components/nsExtensionManager.js
%{_iceapedir}/components/nsFilePicker.js
%{_iceapedir}/components/nsHandlerService.js
%{_iceapedir}/components/nsHelperAppDlg.js
%{_iceapedir}/components/nsLDAPProtocolHandler.js
%{_iceapedir}/components/nsLivemarkService.js
%{_iceapedir}/components/nsLoginInfo.js
%{_iceapedir}/components/nsLoginManager.js
%{_iceapedir}/components/nsLoginManagerPrompter.js
%{_iceapedir}/components/nsPlacesDBFlush.js
%{_iceapedir}/components/nsProgressDialog.js
%{_iceapedir}/components/nsProxyAutoConfig.js
%{_iceapedir}/components/nsSessionStartup.js
%{_iceapedir}/components/nsSessionStore.js
%{_iceapedir}/components/nsSidebar.js
%{_iceapedir}/components/nsSuiteDownloadManagerUI.js
%{_iceapedir}/components/nsSuiteGlue.js
%{_iceapedir}/components/nsTaggingService.js
%{_iceapedir}/components/nsTryToClose.js
%{_iceapedir}/components/nsTypeAheadFind.js
%{_iceapedir}/components/nsUpdateService.js
%{_iceapedir}/components/nsURLFormatter.js
%{_iceapedir}/components/nsWebHandlerApp.js
%{_iceapedir}/components/pluginGlue.js
%{_iceapedir}/components/smileApplication.js
%{_iceapedir}/components/storage-Legacy.js
%{_iceapedir}/components/storage-mozStorage.js
%{_iceapedir}/components/txEXSLTRegExFunctions.js
%{_iceapedir}/components/WebContentConverter.js

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_iceapedir}/components/compreg.dat
%ghost %{_iceapedir}/components/xpti.dat

%attr(755,root,root) %{_iceapedir}/plugins/libnullplugin.so

%dir %{_datadir}/%{name}/chrome
%{_datadir}/%{name}/chrome/classic.jar
%{_datadir}/%{name}/chrome/comm.jar
%{_datadir}/%{name}/chrome/en-US.jar
%{_datadir}/%{name}/chrome/pippki.jar
%{_datadir}/%{name}/chrome/reporter.jar
%{_datadir}/%{name}/chrome/toolkit.jar

%{_datadir}/%{name}/chrome/icons

%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/greprefs
%{_datadir}/%{name}/modules
%{_datadir}/%{name}/res
%{_datadir}/%{name}/searchplugins

%dir %{_datadir}/%{name}/extensions
%{_datadir}/%{name}/extensions/modern@themes.mozilla.org/chrome/modern.jar
%{_datadir}/%{name}/extensions/modern@themes.mozilla.org/icon.png
%{_datadir}/%{name}/extensions/modern@themes.mozilla.org/install.rdf
%{_datadir}/%{name}/extensions/modern@themes.mozilla.org/preview.png
%{_datadir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}/icon.png
%{_datadir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}/install.rdf
%{_datadir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}/preview.png

%{_pixmapsdir}/iceape.png
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-composer.desktop

%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_iceapedir}/components/libimport.so
%attr(755,root,root) %{_iceapedir}/components/libmail.so
%attr(755,root,root) %{_iceapedir}/components/libmsg*.so

%{_iceapedir}/isp
%{_iceapedir}/components/mail.xpt

%{_iceapedir}/components/glautocomp.js
%{_iceapedir}/components/jsmimeemitter.js
%{_iceapedir}/components/mdn-service.js
%{_iceapedir}/components/newsblog.js
%{_iceapedir}/components/nsAbAutoCompleteMyDomain.js
%{_iceapedir}/components/nsAbAutoCompleteSearch.js
%{_iceapedir}/components/nsAbLDAPAttributeMap.js
%{_iceapedir}/components/nsMailNewsCommandLineHandler.js
%{_iceapedir}/components/nsMsgTraitService.js
%{_iceapedir}/components/nsSMTPProtocolHandler.js
%{_iceapedir}/components/offlineStartup.js
%{_iceapedir}/components/smime-service.js

%{_datadir}/%{name}/chrome/gloda.jar
%{_datadir}/%{name}/chrome/messenger.jar
%{_datadir}/%{name}/chrome/newsblog.jar

%{_desktopdir}/%{name}-mail.desktop

%files addon-enigmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_iceapedir}/components/libenigmime.so
%attr(755,root,root) %{_iceapedir}/components/libipc.so
%{_iceapedir}/components/enigmail.js
%{_iceapedir}/components/enigprefs-service.js
%{_iceapedir}/components/enigMsgCompFields.js
%{_datadir}/%{name}/chrome/en-US.jar
%{_datadir}/%{name}/chrome/enigmail.jar
%{_datadir}/%{name}/chrome/enigmime.jar

%files chat
%defattr(644,root,root,755)
%{_desktopdir}/%{name}-chat.desktop
%{_datadir}/%{name}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}/chrome/chatzilla.jar
%{_datadir}/%{name}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}/chrome/icons/default/chatzilla-window.xpm
%{_datadir}/%{name}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}/chrome/icons/default/chatzilla-window16.xpm
%{_datadir}/%{name}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}/components/chatzilla-service.js
%{_datadir}/%{name}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}/install.rdf

%files js-debugger
%defattr(644,root,root,755)
%{_desktopdir}/%{name}-venkman.desktop
%{_datadir}/%{name}/extensions/{f13b157f-b174-47e7-a34d-4815ddfdfeb8}/chrome/venkman.jar
%{_datadir}/%{name}/extensions/{f13b157f-b174-47e7-a34d-4815ddfdfeb8}/components/venkman-service.js
%{_datadir}/%{name}/extensions/{f13b157f-b174-47e7-a34d-4815ddfdfeb8}/install.rdf

%files dom-inspector
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/inspector@mozilla.org/chrome/inspector.jar
%{_datadir}/%{name}/extensions/inspector@mozilla.org/components/inspector-cmdline.js
%{_datadir}/%{name}/extensions/inspector@mozilla.org/defaults/preferences/inspector.js
%{_datadir}/%{name}/extensions/inspector@mozilla.org/install.rdf
%{_datadir}/%{name}/extensions/inspector@mozilla.org/platform/Linux/chrome/icons/default/winInspectorMain.xpm
%{_datadir}/%{name}/extensions/inspector@mozilla.org/platform/Linux/chrome/icons/default/winInspectorMain16.xpm

%if %{with gnomevfs}
%files gnomevfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_iceapedir}/components/libnkgnomevfs.so
%endif
