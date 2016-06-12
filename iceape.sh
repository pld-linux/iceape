#!/bin/sh
# based on script by (c) vip at linux.pl, wolf at pld-linux.org

ICEAPE="@LIBDIR@/iceape/iceape"
PWD=${PWD:-$(pwd)}

if [ -z "$1" ]; then
	exec $ICEAPE
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
