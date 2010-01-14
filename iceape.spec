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
%define	enigmail_ver	0.96.0
Summary:	Iceape - web browser
Summary(es.UTF-8):	Navegador de Internet Iceape
Summary(pl.UTF-8):	Iceape - przeglądarka WWW
Summary(pt_BR.UTF-8):	Navegador Iceape
Name:		iceape
Version:	1.1.18
Release:	3
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/seamonkey-%{version}.source.tar.bz2
# Source0-md5:	ef4455becf3a12833dca7dd92854aeaa
Source1:	http://www.mozilla-enigmail.org/download/source/enigmail-%{enigmail_ver}.tar.gz
# Source1-md5:	cf8c38e8d33965706df383ab33b3923c
Source2:	%{name}-branding.tar.bz2
# Source2-md5:	841caa8235c5350737c09fbbc681e9d3
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
Patch9:		%{name}-pld-branding.patch
Patch10:	%{name}-sqlite.patch
URL:		http://www.pld-linux.org/Packages/Iceape
BuildRequires:	automake
%{?with_svg:BuildRequires:	cairo-devel >= 1.0.0}
BuildRequires:	freetype-devel >= 1:2.1.8
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.0.0}
BuildRequires:	gtk+2-devel
BuildRequires:	libIDL-devel >= 0.8.0
%{?with_gnomeui:BuildRequires:	libgnomeui-devel >= 2.0}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.7
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.6.1
BuildRequires:	nss-devel >= 1:3.11.3
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	pkgconfig
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.356
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.1
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zip >= 2.1
BuildRequires:	zlib-devel >= 1.2.3
Requires:	browser-plugins >= 2.0
%{?with_svg:Requires:	cairo >= 1.0.0}
Requires:	nspr >= 1:4.6.1
Requires:	nss >= 1:3.11.3
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
cd mozilla
/bin/sh %{SOURCE3}
tar -jxf %{SOURCE2}
tar -C mailnews/extensions -zxf %{SOURCE1}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if "%{pld_release}" == "ti"
%patch5 -p1
%else
%patch6 -p1
%endif
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
cd mozilla

cp -f /usr/share/automake/config.* build/autoconf
cp -f /usr/share/automake/config.* nsprpub/build/autoconf
cp -f /usr/share/automake/config.* directory/c-sdk/config/autoconf
ac_cv_visibility_pragma=no; export ac_cv_visibility_pragma
%configure2_13 \
	%{!?debug:--disable-debug} \
	--disable-elf-dynstr-gc \
	%{!?with_gnomeui:--disable-gnomeui} \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	--disable-pedantic \
	--disable-tests \
	--disable-xterm-updates \
	--enable-application=suite \
	--enable-crypto \
	--enable-default-toolkit=gtk2 \
	--enable-extensions \
	--enable-ldap \
	--enable-mathml \
	--enable-optimize="%{rpmcflags}" \
	--enable-postscript \
	%{?with_svg:--enable-svg --enable-svg-renderer-cairo} \
	%{?with_svg:--enable-system-cairo} \
	--enable-xft \
	--enable-xinerama \
	--enable-xprint \
	--enable-old-abi-compat-wrappers \
	--with-default-mozilla-five-home=%{_iceapedir} \
	--with-pthreads \
	--with-system-jpeg \
	--with-system-nspr \
	--with-system-nss \
	--with-system-png \
	--with-system-zlib \
	--with-x

%{__make}

cd mailnews/extensions/enigmail
./makemake -r
%{__make}
cd ../../..

%install
rm -rf $RPM_BUILD_ROOT
cd mozilla
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_datadir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,dictionaries,icons,greprefs,res,searchplugins} \
	$RPM_BUILD_ROOT%{_iceapedir}/{components,plugins}

# preparing to create register
# remove empty directory trees
rm -fr dist/bin/chrome/{US,chatzilla,classic,comm,content-packs,cview,embed,embed-sample,en-US,en-mac,en-unix,en-win,help,inspector,messenger,modern,pipnss,pippki,toolkit,venkman,xmlterm}
# non-unix
rm -f dist/bin/chrome/en-{mac,win}.jar

# creating and installing register
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regxpcom
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regchrome

ln -sf ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_chromedir}
ln -sf ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_iceapedir}/defaults
ln -sf ../../share/%{name}/dictionaries $RPM_BUILD_ROOT%{_iceapedir}/dictionaries
ln -sf ../../share/%{name}/greprefs $RPM_BUILD_ROOT%{_iceapedir}/greprefs
ln -sf ../../share/%{name}/icons $RPM_BUILD_ROOT%{_iceapedir}/icons
ln -sf ../../share/%{name}/res $RPM_BUILD_ROOT%{_iceapedir}/res
ln -sf ../../share/%{name}/searchplugins $RPM_BUILD_ROOT%{_iceapedir}/searchplugins

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/{[!m],m[!y]}*	$RPM_BUILD_ROOT%{_iceapedir}/components
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
cp -frL dist/bin/dictionaries/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/dictionaries
cp -frL dist/bin/greprefs/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins

install dist/bin/*.so $RPM_BUILD_ROOT%{_iceapedir}

ln -s %{_libdir}/libnssckbi.so $RPM_BUILD_ROOT%{_iceapedir}/libnssckbi.so

install %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
	$RPM_BUILD_ROOT%{_desktopdir}

install suite/branding/icons/gtk/iceape.png $RPM_BUILD_ROOT%{_pixmapsdir}

install dist/bin/iceape-bin $RPM_BUILD_ROOT%{_iceapedir}
install dist/bin/regchrome $RPM_BUILD_ROOT%{_iceapedir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_iceapedir}
install dist/bin/xpidl $RPM_BUILD_ROOT%{_iceapedir}

cp $RPM_BUILD_ROOT%{_chromedir}/installed-chrome.txt \
        $RPM_BUILD_ROOT%{_chromedir}/%{name}-installed-chrome.txt

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

MOZILLA_FIVE_HOME=%{_iceapedir} %{_iceapedir}/regxpcom
MOZILLA_FIVE_HOME=%{_iceapedir} %{_iceapedir}/regchrome
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
%dir %{_iceapedir}/greprefs
%dir %{_iceapedir}/icons
%dir %{_iceapedir}/plugins
%dir %{_iceapedir}/res
%dir %{_iceapedir}/searchplugins
%dir %{_datadir}/%{name}

%attr(755,root,root) %{_iceapedir}/libxpcom.so
%attr(755,root,root) %{_iceapedir}/libxpcom_compat.so
%attr(755,root,root) %{_iceapedir}/libxpcom_core.so
%attr(755,root,root) %{_iceapedir}/libgfxpsshar.so
%attr(755,root,root) %{_iceapedir}/libgkgfx.so
%attr(755,root,root) %{_iceapedir}/libgtkembedmoz.so
%attr(755,root,root) %{_iceapedir}/libgtkxtbin.so
%attr(755,root,root) %{_iceapedir}/libjsj.so
%attr(755,root,root) %{_iceapedir}/libldap50.so
%attr(755,root,root) %{_iceapedir}/libprldap50.so
%attr(755,root,root) %{_iceapedir}/libssldap50.so
%attr(755,root,root) %{_iceapedir}/libmozjs.so
%attr(755,root,root) %{_iceapedir}/libxpistub.so
%attr(755,root,root) %{_iceapedir}/libxlibrgb.so

%attr(755,root,root) %{_iceapedir}/iceape-bin
%attr(755,root,root) %{_iceapedir}/reg*
%attr(755,root,root) %{_iceapedir}/xpidl

%attr(755,root,root) %{_iceapedir}/libnssckbi.so

%attr(755,root,root) %{_iceapedir}/components/libaccess*.so
%attr(755,root,root) %{_iceapedir}/components/libappcomps.so
%attr(755,root,root) %{_iceapedir}/components/libauth*.so
%attr(755,root,root) %{_iceapedir}/components/libautoconfig.so
%attr(755,root,root) %{_iceapedir}/components/libcaps.so
%attr(755,root,root) %{_iceapedir}/components/libchrome.so
%attr(755,root,root) %{_iceapedir}/components/libcomposer.so
%attr(755,root,root) %{_iceapedir}/components/libcookie.so
%attr(755,root,root) %{_iceapedir}/components/libdocshell.so
%attr(755,root,root) %{_iceapedir}/components/libeditor.so
%attr(755,root,root) %{_iceapedir}/components/libembedcomponents.so
%attr(755,root,root) %{_iceapedir}/components/libfileview.so
%attr(755,root,root) %{_iceapedir}/components/libgfx*.so
%attr(755,root,root) %{_iceapedir}/components/libgk*.so
%attr(755,root,root) %{_iceapedir}/components/libhtmlpars.so
%attr(755,root,root) %{_iceapedir}/components/libi18n.so
%attr(755,root,root) %{_iceapedir}/components/libimg*.so
%attr(755,root,root) %{_iceapedir}/components/libjar50.so
%attr(755,root,root) %{_iceapedir}/components/libjsd.so
%attr(755,root,root) %{_iceapedir}/components/libmork.so
%attr(755,root,root) %{_iceapedir}/components/libmoz*.so
%attr(755,root,root) %{_iceapedir}/components/libmyspell.so
%attr(755,root,root) %{_iceapedir}/components/libnecko*.so
%attr(755,root,root) %{_iceapedir}/components/libnkdatetime.so
%attr(755,root,root) %{_iceapedir}/components/libnkfinger.so
%attr(755,root,root) %{_iceapedir}/components/libns*.so
%attr(755,root,root) %{_iceapedir}/components/liboji.so
%attr(755,root,root) %{_iceapedir}/components/libp3p.so
%attr(755,root,root) %{_iceapedir}/components/libpermissions.so
%attr(755,root,root) %{_iceapedir}/components/libpipboot.so
%attr(755,root,root) %{_iceapedir}/components/libpipnss.so
%attr(755,root,root) %{_iceapedir}/components/libpippki.so
%attr(755,root,root) %{_iceapedir}/components/libpref.so
%attr(755,root,root) %{_iceapedir}/components/libprofile.so
%attr(755,root,root) %{_iceapedir}/components/librdf.so
%attr(755,root,root) %{_iceapedir}/components/libremoteservice.so
%attr(755,root,root) %{_iceapedir}/components/libschemavalidation.so
%attr(755,root,root) %{_iceapedir}/components/libsearchservice.so
%attr(755,root,root) %{_iceapedir}/components/libspellchecker.so
%attr(755,root,root) %{_iceapedir}/components/libsql.so
%attr(755,root,root) %{_iceapedir}/components/libsroaming.so
%attr(755,root,root) %{_iceapedir}/components/libstoragecomps.so
%attr(755,root,root) %{_iceapedir}/components/libsystem-pref.so
%attr(755,root,root) %{_iceapedir}/components/libtransformiix.so
%attr(755,root,root) %{_iceapedir}/components/libtxmgr.so
%attr(755,root,root) %{_iceapedir}/components/libtypeaheadfind.so
%attr(755,root,root) %{_iceapedir}/components/libuconv.so
%attr(755,root,root) %{_iceapedir}/components/libucv*.so
%attr(755,root,root) %{_iceapedir}/components/libuniversalchardet.so
%attr(755,root,root) %{_iceapedir}/components/libwallet.so
%attr(755,root,root) %{_iceapedir}/components/libwalletviewers.so
%attr(755,root,root) %{_iceapedir}/components/libwebbrwsr.so
%attr(755,root,root) %{_iceapedir}/components/libwebsrvcs.so
%attr(755,root,root) %{_iceapedir}/components/libwidget_gtk2.so
%attr(755,root,root) %{_iceapedir}/components/libx*.so

%{_iceapedir}/components/access*.xpt
%{_iceapedir}/components/alerts.xpt
%{_iceapedir}/components/appshell.xpt
%{_iceapedir}/components/appstartup.xpt
%{_iceapedir}/components/autocomplete.xpt
%{_iceapedir}/components/autoconfig.xpt
%{_iceapedir}/components/bookmarks.xpt
%{_iceapedir}/components/caps.xpt
%{_iceapedir}/components/chardet.xpt
%{_iceapedir}/components/chrome.xpt
%{_iceapedir}/components/commandhandler.xpt
%{_iceapedir}/components/composer.xpt
%{_iceapedir}/components/content*.xpt
%{_iceapedir}/components/cookie.xpt
%{_iceapedir}/components/directory.xpt
%{_iceapedir}/components/docshell.xpt
%{_iceapedir}/components/dom*.xpt
%{_iceapedir}/components/downloadmanager.xpt
%{_iceapedir}/components/editor.xpt
%{_iceapedir}/components/embed_base.xpt
%{_iceapedir}/components/extensions.xpt
%{_iceapedir}/components/exthandler.xpt
%{_iceapedir}/components/find.xpt
%{_iceapedir}/components/filepicker.xpt
%{_iceapedir}/components/gfx*.xpt
%{?with_svg:%{_iceapedir}/components/gksvgrenderer.xpt}
%{_iceapedir}/components/history.xpt
%{_iceapedir}/components/htmlparser.xpt
%{?with_gnomeui:%{_iceapedir}/components/imgicon.xpt}
%{_iceapedir}/components/imglib2.xpt
%{_iceapedir}/components/intl.xpt
%{_iceapedir}/components/jar.xpt
%{_iceapedir}/components/js*.xpt
%{_iceapedir}/components/layout*.xpt
%{_iceapedir}/components/locale.xpt
%{_iceapedir}/components/lwbrk.xpt
%{_iceapedir}/components/mimetype.xpt
%{_iceapedir}/components/moz*.xpt
%{_iceapedir}/components/necko*.xpt
%{_iceapedir}/components/oji.xpt
%{_iceapedir}/components/p3p.xpt
%{_iceapedir}/components/pipboot.xpt
%{_iceapedir}/components/pipnss.xpt
%{_iceapedir}/components/pippki.xpt
%{_iceapedir}/components/plugin.xpt
%{_iceapedir}/components/pref.xpt
%{_iceapedir}/components/prefetch.xpt
%{_iceapedir}/components/prefmigr.xpt
%{_iceapedir}/components/profile.xpt
%{_iceapedir}/components/progressDlg.xpt
%{_iceapedir}/components/proxyObjInst.xpt
%{_iceapedir}/components/rdf.xpt
%{_iceapedir}/components/related.xpt
%{_iceapedir}/components/saxparser.xpt
%{_iceapedir}/components/search.xpt
%{_iceapedir}/components/schemavalidation.xpt
%{_iceapedir}/components/shistory.xpt
%{_iceapedir}/components/signonviewer.xpt
%{_iceapedir}/components/spellchecker.xpt
%{_iceapedir}/components/sql.xpt
%{_iceapedir}/components/storage.xpt
%{_iceapedir}/components/toolkitremote.xpt
%{_iceapedir}/components/txmgr.xpt
%{_iceapedir}/components/txtsvc.xpt
%{_iceapedir}/components/typeaheadfind.xpt
%{_iceapedir}/components/uconv.xpt
%{_iceapedir}/components/unicharutil.xpt
%{_iceapedir}/components/uriloader.xpt
%{_iceapedir}/components/urlformatter.xpt
%{_iceapedir}/components/wallet*.xpt
%{_iceapedir}/components/webBrowser_core.xpt
%{_iceapedir}/components/webbrowserpersist.xpt
%{_iceapedir}/components/webshell_idls.xpt
%{_iceapedir}/components/websrvcs.xpt
%{_iceapedir}/components/widget.xpt
%{_iceapedir}/components/windowds.xpt
%{_iceapedir}/components/windowwatcher.xpt
%{_iceapedir}/components/x*.xpt

%{_iceapedir}/components/jsconsole-clhandler.js
%{_iceapedir}/components/nsCloseAllWindows.js
%{_iceapedir}/components/nsComposerCmdLineHandler.js
%{_iceapedir}/components/nsDictionary.js
%{_iceapedir}/components/nsDownloadProgressListener.js
%{_iceapedir}/components/nsFilePicker.js
%{_iceapedir}/components/nsHelperAppDlg.js
%{_iceapedir}/components/nsInterfaceInfoToIDL.js
%{_iceapedir}/components/nsKillAll.js
%{_iceapedir}/components/nsProgressDialog.js
%{_iceapedir}/components/nsProxyAutoConfig.js
%{_iceapedir}/components/nsResetPref.js
%{_iceapedir}/components/nsSchemaValidatorRegexp.js
%{_iceapedir}/components/nsSidebar.js
%{_iceapedir}/components/nsUpdateNotifier.js
%{_iceapedir}/components/nsURLFormatter.js
%{_iceapedir}/components/nsXmlRpcClient.js
%{_iceapedir}/components/xulappinfo.js

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_iceapedir}/components/compreg.dat
%ghost %{_iceapedir}/components/xpti.dat

%dir %{_datadir}/%{name}/chrome
%{_datadir}/%{name}/chrome/US.jar
%{_datadir}/%{name}/chrome/classic.jar
%{_datadir}/%{name}/chrome/comm.jar
%{_datadir}/%{name}/chrome/content-packs.jar
%{_datadir}/%{name}/chrome/cview.jar
%{_datadir}/%{name}/chrome/embed-sample.jar
%{_datadir}/%{name}/chrome/en-US.jar
%{_datadir}/%{name}/chrome/en-unix.jar
%{_datadir}/%{name}/chrome/help.jar
%{_datadir}/%{name}/chrome/layoutdebug.jar
%{_datadir}/%{name}/chrome/modern.jar
%{_datadir}/%{name}/chrome/pipnss.jar
%{_datadir}/%{name}/chrome/pippki.jar
%{_datadir}/%{name}/chrome/reporter.jar
%{_datadir}/%{name}/chrome/sql.jar
%{_datadir}/%{name}/chrome/sroaming.jar
%{_datadir}/%{name}/chrome/tasks.jar
%{_datadir}/%{name}/chrome/toolkit.jar
%{_datadir}/%{name}/chrome/xforms.jar

%ghost %{_datadir}/%{name}/chrome/chrome.rdf
%ghost %{_datadir}/%{name}/chrome/overlays.rdf
# not generated automatically ?
%{_datadir}/%{name}/chrome/stylesheets.rdf
%{_datadir}/%{name}/chrome/chromelist.txt
%{_datadir}/%{name}/chrome/icons
%exclude %{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/chatzilla-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm

%{_datadir}/%{name}/chrome/%{name}-installed-chrome.txt
%ghost %{_datadir}/%{name}/chrome/installed-chrome.txt

%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/dictionaries
%{_datadir}/%{name}/greprefs
%exclude %{_datadir}/%{name}/defaults/pref/inspector.js
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/res
%{_datadir}/%{name}/searchplugins

%{_pixmapsdir}/iceape.png
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/%{name}-composer.desktop

%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_iceapedir}/libmsgbaseutil.so
%attr(755,root,root) %{_iceapedir}/components/libaddrbook.so
%attr(755,root,root) %{_iceapedir}/components/libbayesflt.so
%attr(755,root,root) %{_iceapedir}/components/libimpText.so
%attr(755,root,root) %{_iceapedir}/components/libimpComm4xMail.so
%attr(755,root,root) %{_iceapedir}/components/libimport.so
%attr(755,root,root) %{_iceapedir}/components/liblocalmail.so
%attr(755,root,root) %{_iceapedir}/components/libmailnews.so
%attr(755,root,root) %{_iceapedir}/components/libmailview.so
%attr(755,root,root) %{_iceapedir}/components/libmime.so
%attr(755,root,root) %{_iceapedir}/components/libmimeemitter.so
%attr(755,root,root) %{_iceapedir}/components/libmsg*.so
%attr(755,root,root) %{_iceapedir}/components/libvcard.so

%{_iceapedir}/components/addrbook.xpt
%{_iceapedir}/components/impComm4xMail.xpt
%{_iceapedir}/components/import.xpt
%{_iceapedir}/components/mailnews.xpt
%{_iceapedir}/components/mailview.xpt
%{_iceapedir}/components/mime.xpt
%{_iceapedir}/components/msg*.xpt

%{_iceapedir}/components/mdn-service.js
%{_iceapedir}/components/nsAbLDAPAttributeMap.js
%{_iceapedir}/components/nsLDAPPrefsService.js
%{_iceapedir}/components/offlineStartup.js
%{_iceapedir}/components/smime-service.js

%{_datadir}/%{name}/chrome/messenger.jar

%{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm

%{_desktopdir}/%{name}-mail.desktop

%files addon-enigmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_iceapedir}/components/libenigmime.so
%attr(755,root,root) %{_iceapedir}/components/libipc.so
%{_iceapedir}/components/enigmail.xpt
%{_iceapedir}/components/enigmime.xpt
%{_iceapedir}/components/ipc.xpt
%{_iceapedir}/components/enigmail.js
%{_iceapedir}/components/enigprefs-service.js
%{_iceapedir}/components/enigMsgCompFields.js
%{_datadir}/%{name}/chrome/enigmail-en-US.jar
%{_datadir}/%{name}/chrome/enigmail-locale.jar
%{_datadir}/%{name}/chrome/enigmail-skin-seamonkey.jar
%{_datadir}/%{name}/chrome/enigmail-skin.jar
%{_datadir}/%{name}/chrome/enigmail.jar
%{_datadir}/%{name}/chrome/enigmime.jar

%files chat
%defattr(644,root,root,755)
%{_iceapedir}/components/chatzilla-service.js
%{_datadir}/%{name}/chrome/chatzilla.jar
%{_datadir}/%{name}/chrome/icons/default/chatzilla-window*.xpm
%{_desktopdir}/%{name}-chat.desktop

%files js-debugger
%defattr(644,root,root,755)
%{_iceapedir}/components/venkman-service.js
%{_datadir}/%{name}/chrome/venkman.jar
%{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%{_desktopdir}/%{name}-venkman.desktop

%files dom-inspector
%defattr(644,root,root,755)
%{_iceapedir}/components/inspector.xpt
%{_iceapedir}/components/inspector-cmdline.js
%{_datadir}/%{name}/chrome/inspector.jar
%{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm
%{_datadir}/%{name}/defaults/pref/inspector.js

%if %{with gnomevfs}
%files gnomevfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_iceapedir}/components/libnkgnomevfs.so
%endif
