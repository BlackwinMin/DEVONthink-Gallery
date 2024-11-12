#!/bin/sh
#
# LaunchBar Action Script
#
PATH=$PATH:/usr/local/bin/;
echo "$# arguments passed"

for ARG in "$@"; do
# 创建alias替身文件
osascript <<EOF
set fFolder to POSIX file "/Users/Min/Databases/OCR" as alias
set fFile to POSIX file "$ARG" as alias
tell application "Finder"
make new alias file to fFile at fFolder
end tell
EOF
done