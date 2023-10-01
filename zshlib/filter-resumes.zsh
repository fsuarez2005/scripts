#!/bin/zsh


RESUMEDIR="/Users/franksuarez/Desktop/save"
cd "$RESUMEDIR"

TARGETDIR="$HOME/Desktop/resume"



testfunction () {
	DIRECTORY="$(dirname "$1")"
	
	FILENAME="$(basename "$1")"
	
	EXT="$(echo $FILENAME|sed -n "s/.*\.\([^.]\{1,200\}\)$/\1/p")"
	
	MD5="$(md5 -q "$1")"
	
	BDATE="$(stat -t "%Y%m%d" -f "%Sm" ${REPLY})"
	
	TARGETFILE="${TARGETDIR}/resume-${BDATE}-${MD5}.${EXT}"
	
	cp -v ${REPLY} ${TARGETFILE}
}



main () {
	gfind -type f -iname '*resume*'|while read; do
		testfunction "$REPLY"
	done
}

main
