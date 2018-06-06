#!/bin/bash

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

####Senthil360 - XDA-developers.com#####
#<senthilmanikandan360@gmail.com>#

#The name of file to search is $1
#The word/string/char to search is $2
#Example = bash split_check.sh movie_list.txt Gladiator

#Split files are kept in a separate 'split_output' folder

file=$1
word=$2
div="================"
if [ -d split_output ]; then
   rm -rf split_output/*
   cp $file split_output/$file
   cd split_output
elif [ ! -d split_output ]; then
   mkdir split_output
   cp $file split_output/$file
   cd split_output
fi
split -b 10k $file
rm -f $file
x=$(ls)
file_arr=()
for i in $x; do
   if grep -q "$word" $i; then
      echo $div
      echo "Found in : $i"
      file_arr+=("$i")
      echo $div
   else
      echo "Not found in : $i"
   fi
done

echo ""

for j in ${file_arr[@]}; do
   echo -e "Processing ${G} $j ${N} file.."
   sleep 1.2
   echo "" 
   grep --color=always -o "$word" $j | head -n 1
   echo ""
   echo "Total occurrence of $word = $(grep -o "$word" $j | wc -l)"
done