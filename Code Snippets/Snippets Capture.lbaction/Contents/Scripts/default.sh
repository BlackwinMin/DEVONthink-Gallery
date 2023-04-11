#!/bin/sh
#
# LaunchBar Action Script
#

l="bash"

for ARG in "$@"; do
    
    read -r -d '' applescriptCode1 <<'EOF'
    set n to text returned of (display dialog "请输入片段名" default answer "")
    return n
EOF
    
    read -r -d '' applescriptCode2 <<'EOF'
    tell application "System Events"
        set nameList to {"AppleScript","BASH","HTML","Python","Javascript","MathJax","URL Scheme","macOS Path"}
EOF
    
    n=$(osascript -e "$applescriptCode1")
    l=$(osascript -e "$applescriptCode2")
    
    echo "$ARG" | sed -e "1 s/.*/\`\`\`$l\n&/" -e "$ s/.*/&\n\`\`\`/" > "/Users/min/Databases/T000/Script/"$l"/""$n"".md"
done && afplay "/System/Library/Sounds/Purr.aiff"