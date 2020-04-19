#!/bin/bash 

#not complete !!!!!!!!!!!!!!!!!!!


sleep_f () { sleep 0.3s ; }
sleep_f1 () { sleep 1s ; }

red () { echo -e  "\033[1;39m " ; } 
white () { echo -e  "\033[1;97m " ; } 

sleep_f 
clear
white
echo -e "\t \t -------"
sleep_f 
echo -e "\t \t|  WEP  |"
sleep_f 
echo -e "\t \t -------"
sleep_f 
echo -e "\t\t\t \0 -v 0.5" 
sleep_f 
echo -e "\t\t\t \033[5m-By AlenPaulVarghese\033[0m"


sleep_f 

dpkg -l "aircrack-ng" > /dev/null 2>&1
if [ $? = '0' ]
then 
        white
	printf "[*] Package is installed\n"
sleep_f
	printf "\n"
sleep_f
	white
	printf "[1] Yes\n"
sleep_f
	printf "[2] No\n"
sleep_f
    read -p "Your Selection : "  need
	if [ $need = '1' ]
	then
	   printf "installing"
		gnome-terminal -e "sudo apt install aircrack-ng" > /dev/null 2>&1
	elif [ $need = '2' ] 
	 then
		printf "Exiting Script......"
	else
		red
		printf "[!] invalid option"
		white
		sleep_f1
		sudo ./WEP.sh
	   fi
elif [ $? = '1' ]
then
    printf "package is not installed"
    printf "Do u want to install the package"
    printf "[1]Yes"
    printf "[2]No"
fi
echo -e "\n"



