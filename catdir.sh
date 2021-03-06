#!/bin/bash ##CHANGE this to "#!/system/bin/sh" if your ROM doesn't have "bash" inbuilt

##Senthil360 @XDA-developers.com##

#USAGE :-  sh catdir "Directory location"
#Example - to view the values of all tunables of interactive governor - - sh /sdcard/catdir "/sys/devices/system/cpu/cpu2/cpufreq/interactive"

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

###cpu0 = Your LITTLE cpu
sca_gov_l=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor)
###cpu2 = Your big cpu
sca_gov_b=$(cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor)

dir=$1
if [ "$dir" = "vm" ]; then
    dir=/proc/sys/vm
elif [ "$dir" = "little" ]; then
    dir=/sys/devices/system/cpu/cpu0/cpufreq/$sca_gov_l
elif [ "$dir" = "big" ]; then
     dir=/sys/devices/system/cpu/cpu2/cpufreq/$sca_gov_b
fi

cd $dir

a=1; Col="${C}"
echo -e "${G}=================${N}"
echo -e "${V}$dir${N}"
echo -e "${G}=================${N}"
echo ""

if [ -e /sdcard/dtmp ]; then
    rm -f /sdcard/dtmp
fi

for i in $(ls); do
     echo -e "$Col$a-$i${N} : ${Y}$($BB cat $i 2>/dev/null)${N}" 2>/dev/null
     echo "$a-$i-$($BB cat $i 2>/dev/null)" 1>>/sdcard/dtmp
     echo ""
  a=$((a+1))
done



