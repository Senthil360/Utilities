#!/system/bin/sh

##<Senthil360 @XDA-developers.com>##
###Usage 
#   bash pullAPK.sh b  = For Backing up all user apps
#   bash pullAPK.sh r = For restoring backup up apps

opt=$1

backupApp() {
cd /data/app
a=1
total=$(find /data/app/ -maxdepth 1 -type d -print| wc -l)
echo "Total is $total"
while [ $a -lt $total ]; do
   list=$(ls | cut -d ' ' -f$a | head -n $a | tail -n 1)
   echo $list
   cd $list
   cp *.apk /sdcard/APK/$a.apk
   cd ..
   unset list;
a=$(($a+1))
echo "Copied $a APK(s)"
done
}

restoreApp() {
b=1
total_app=$(ls | wc -l)
while [ $b -lt $total_app ]; do
   pm install $b.apk
b=$(($b+1))
done
}

if [ "$opt" = "b" ]; then
   backupApp
elif [ "$opt" = "r" ]; then
   restoreApp
fi