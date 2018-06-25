#!/system/bin/sh

##Senthil360 @XDA-developers.com##

#USAGE :-  sh adb_br.sh options [Port number(default 7777)] 

# colors
G='\e[01;32m'
R='\e[01;31m'
N='\e[00;37;40m'
Y='\e[01;33m'
B='\e[01;34m'
V='\e[01;35m'
Bl='\e[01;30m'
C='\e[01;36m'
W='\e[01;37m'
div="    ================    "
echo ""
echo -e "        ${R}ADB Backup Script${N}           "
sleep 0.8
echo ""
echo -e "${C} $div${N}"
echo ""
echo -e "${W}Allow the device at${N} ${G}RSA keys${N} ${W}prompt${N}"
echo "."
sleep 1.5
echo -e "${W}Create your${N} ${G}Password ${N} ${W}when you are asked to${N}"
echo "."
sleep 1.5
echo -e "${C} $div${N}"

createDir() {
cd /sdcard
mkdir ADB
cd ADB
mkdir Backup
echo -e "${W}Backup Directory has been created at${N} ${R}/sdcard/ADB/Backup${N}"
} 

if [ ! -d /sdcard/ADB/Backup ]; then
   createDir
fi

adbEssentials() {
port_no=$1
if [ $# -eq 0 ]; then
    port_no=7777
fi
check_port=$(getprop | grep "service.adb.tcp.port" | cut -d ':' -f2 | cut -d '[' -f2 | cut -d ']' -f1)
if [ $port_no -ne $check_port ]; then
   setprop service.adb.tcp.port $port_no
fi
echo -e "${W}Killing and Rebooting the ADB server${N}"
sleep 2
adb start-server
sleep 2
adb connect localhost:$port_no
} 


startBackup() {
adb backup -apk -noshared -nosystem -all -f /sdcard/ADB/Backup/$(date | tr -d ' ' ).ab
}

adbEssentials
sleep 7
startBackup