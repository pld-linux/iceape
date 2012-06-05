#!/bin/sh
# based on script by (c) vip at linux.pl, wolf at pld-linux.org

LIBDIR="@LIBDIR@/iceape"

ICEAPE="$LIBDIR/iceape"
PWD=${PWD:-$(pwd)}

if [ "$1" = "-remote" ]; then
	exec $ICEAPE "$@"
else
	if ! $ICEAPE -remote 'ping()' 2>/dev/null; then
		if [ -f "$PWD/$1" ]; then
			exec $ICEAPE "file://$PWD/$1"
		else
			exec $ICEAPE "$@"
		fi
	else
		if [ -z "$1" ]; then
			exec $ICEAPE -remote 'xfeDoCommand(openBrowser)'
		elif [ "$1" = "-mail" ]; then
			exec $ICEAPE -remote 'xfeDoCommand(openInbox)'
		elif [ "$1" = "-compose" -o "$1" = "-editor" ]; then
			exec $ICEAPE -remote 'xfeDoCommand(composeMessage)'
		else
			if [ -f "$PWD/$1" ]; then
				URL="file://$PWD/$1"
			else
				URL="$1"
			fi
			if ! grep -q browser.tabs.opentabfor.middleclick.*false ~/.mozilla/seamonkey/*/prefs.js; then
				exec $ICEAPE -new-tab "$URL"
			else
				exec $ICEAPE -new-window "$URL"
			fi
		fi
	fi
fi
