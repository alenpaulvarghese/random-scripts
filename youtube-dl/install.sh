#!/bin/bash 
# (c) starktm1 a.k.a AlenPaulVarghese

red () { echo -e  "\033[1;31m " ; } 
white () { echo -e  "\033[1;97m " ; }
green () { echo -e  "\033[1;32m " ; }
sleep_f1 () { sleep 1s ; }
FILEPATH='youtube-downloader.py'
green
echo '[*] Processing..'
wget https://raw.githubusercontent.com/alenpaul2001/python-script/master/youtube-dl/youtube-downloader.py > /dev/null 2>&1 
sleep_f1
if test -f "$FILEPATH"; then
    green
    echo '[$] Download Complete ..'
else 
    red
    echo '[!] Error..' 
fi
white
sudo chmod 777 $FILEPATH
green
echo '[*] Processing...'
sudo mv $FILEPATH /usr/local/bin/youtube
echo ''
echo '[$] Succefully Installed'
white
echo '(c) AlenPaulVarghese'