#!/usr/bin/zsh

set -e

is_puzzle_directory() {
  f=$1
  test -d "$f" -a -f "$f/Makefile" -a -f "$f/README.md"
}

TARGET="README.md"

rm -f $TARGET
echo "Adding head"
cat helpers/puzzle_head.md > $TARGET
echo "<!-- The following is AUTO-GENERATED by $0 - see 'make doc' -->" >> $TARGET 

for file_or_dir in *
do
	if is_puzzle_directory $file_or_dir
	then
		d=$file_or_dir
		echo "Adding $d"
    		echo "* [$d]($d/)" >> $TARGET
	fi
done