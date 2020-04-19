#!/bin/bash 
# (c) starktm1 a.k.a AlenPaulVarghese

red () { echo -e  "\033[1;31m " ; } 
white () { echo -e  "\033[1;97m " ; }
green () { echo -e  "\033[1;32m " ; }
sleep_f1 () { sleep 1s ; }

cd $HOME

FILEPATH='auto_wallpaper.py'
FILE_TO_CREATE=$HOME'/Pictures/wallpaper'
echo $FILE_TO_CREATE
TEMP=$HOME/.local/share/backgrounds/temp/
CONFIG=$HOME/.config/autostart/autowallpaper.py.desktop
TEMP_FILE='wall.jpeg'
sleep_f1
green
echo '[*] Processing..'
wget https://raw.githubusercontent.com/alenpaul2001/python-script/master/auto_wallpaper.py > /dev/null 2>&1 
sleep_f1
if test -f "$FILEPATH"; then
    green
    echo '[*] Download Complete ..'
else 
    red
    echo '[!] Error..' 
fi

sleep_f1

if test -d "$FILE_TO_CREATE" && test -d "$TEMP" ; then
    green
    echo '[*] Folder Already Exists'
else
    mkdir $FILE_TO_CREATE
    mkdir $TEMP
fi

mv $FILEPATH $FILE_TO_CREATE

wget https://raw.githubusercontent.com/alenpaul2001/python-script/master/archive/wall.jpeg > /dev/null 2>&1 
green
echo '[*] Download Complete ..'
mv wall.jpeg $HOME/.local/share/backgrounds/
echo '[*] Moved Succefully'
gsettings set org.gnome.desktop.background picture-uri "file://$HOME/.local/share/backgrounds/$TEMP_FILE"
sleep_f1
white
echo "Do u wanto set this as autostart"
echo "[1]Yes"
echo "[2]No"
read -p "Your Selection : "  need
if [ $need = '1' ]
	then
cat > $CONFIG <<-ENDOFFILE
[Desktop Entry]
Type=Application
Exec=python3 $HOME/Pictures/wallpaper/auto_wallpaper.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_IN]=$HOME/Pictures/wallpaper/auto_wallpaper.py
Name=$HOME/Pictures/wallpaper/auto_wallpaper.py
Comment[en_IN]=(c) AlenPaulVarghese
Comment=(c) AlenPaulVarghese
ENDOFFILE
elif [ $need = '2' ] 
	then
        red
		printf "Exiting Script......"
        echo "manualy execute the file Pictures/wallpaper/auto_wallpaper.py"
        echo "(c) AlenPaulVarghese"
        exit
fi 

echo "Copy Your Favourite Pictures Into /Pictures/wallpaper Folder"
echo "Open Startup Application to disable autostart feature"
red
echo "[?] Restart Required !"

white
echo "Restart Now?"
echo "[1]Yes"
echo "[2]No"
read -p "Your Selection : "  need
if [ $need = '1' ]
	then
        reboot
        echo "(c) AlenPaulVarghese"
elif [ $need = '2' ] 
	then
		printf "Exiting Script......"
        echo "(c) AlenPaulVarghese"
fi