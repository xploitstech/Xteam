  #!/bin/bash

# colour 
Black="\033[1;30m"       # Black
Red="\033[1;31m"         # Red
Green="\033[1;32m"       # Green
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White

clear
apt-get update
apt-get upgrade
apt-get install python
apt-get install python2
clear
echo -e "$Purple Created By \e[1;34m"
       figlet X TEAM | lolcat
sleep 2.0

echo " "  
figlet -f X TEAM | lolcat

    echo " "
    echo -e "$Red                                 ⫸ Coded by$Yellow xploits$Red ⫷\033[0m"
    echo -e "$Red                               ⫸$Purple X Hackers$Red ⫷\033[0m"
echo " "
echo -e " $Green     |---------------------------------------------------------------------|"
echo -e " $Green     ||----------------------------$Cyan [features] $Green---------------------------||"
echo -e " $Blue     ||                                                                   ||"
echo -e " $Green     ||             $Purple==>$Yellow[1️⃣] Insta information gathering$Green                    ||"
echo -e " $Green     ||             $Purple==>️$Yellow[2️⃣] Crack android lockscreen interfaces$Green            ||"
echo -e " $Green     ||             $Purple==>$Yellow[3️⃣] Phishing hacks$Green                                 ||"
echo -e " $Green     ||             $Purple==>$Yellow[4️⃣] Wireless Attacks[coming soon]$Green                  ||"
echo -e " $Green     ||             $Purple==>$Yellow[5️⃣] Update Xteam$Green                                   ||"
echo -e " $Green     ||             $Purple==>$Yellow[6️⃣] Remove Xteam$Green                                   ||"
echo -e " $Green     ||             $Purple==>$Yellow[7️⃣] About$Green                                          ||"
echo -e " $Green     ||             $Purple==>$Yellow[8️⃣] exit$Green                                           ||"
echo -e " $Green     ||                                                                   ||"                                                                                       
echo -e " $Green     ||---------------------------$Cyan [select option] $Green-----------------------||"
echo -e " $Green     |---------------------------------------------------------------------|"
echo " "
echo " "

    read ch
   if [ $ch -eq 1 ];then
        cd $HOME
        cd Xteam
        cd Ig_information_gathering
        bash start.sh

        exit
    elif [ $ch -eq 2 ];then 
         cd $HOME
         git clone https://github.com/tegal1337/CiLocks
         cd CiLocks
         chmod +x cilocks
         sudo ./cilocks
        
        exit
    elif [ $ch -eq 3 ];then
        git clone git://github.com/htr-tech/zphisher.git
        cd zphisher
        bash zphisher.sh

        exit
    elif [ $ch -eq 4 ];then
        cd $HOME

        exit
    elif [ $ch -eq 5 ];then
        echo -e "\e[1;34m Downloading Latest Files..."
        cd $HOME
        rm -rf Xteam
        git clone https://github.com/xploitstech/Xteam
        cd Xteam
        bash Xteam.sh
     
        exit
   elif [ $ch -eq 6 ];then 
        cd $HOME
        rm -rf Xteam
        
        exit
   elif [ $ch -eq 7 ];then
        echo -e 
        cd $HOME

        exit
        
    else
        echo -e "\e[4;32m Invalid Input !!! \e[0m"
        pause
    fi
done
