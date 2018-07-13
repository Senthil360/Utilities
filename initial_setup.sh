#!/bin/bash
clear;
#colors
G='\033[01;32m'
R='\033[01;31m'
C='\033[01;36m'
B='\033[01;34m'
BR='\033[05;31m'
N='\033[0m'

func_s777() {
   cp s777 /bin/s777
   chmod 777 /bin/s777
}

perm_alias() {
   cd ~
   echo 'alias python="python3"' > ".bashrc"
}

setupGtPython() {
cd ~
if[ ! -d "codes" ]; then
   setupCodesDir
fi
   cd "codes/python"
   git clone https://github.com/Senthil360/gt_python.git
   mkdir "BETA"
   cd "BETA"
   git clone -b BETA https://github.com/Senthil360/gt_python.git
   git checkout BETA
}

setupPythonML(){
cd ~
if[ ! -d "codes" ]; then
   setupCodesDir
fi
   cd "codes/python"
   git clone git@gitlab.com:Senthil360/PythonML.git
}


setupCodesDir() {
cd ~
if [ -d "codes" ]; then
   code=true
elif [ ! -d "codes" ]; then
   code=false
   mkdir "codes"
   chmod 755 codes
   cd "codes"
   mkdir "python"
   mkdir "java"
   mkdir "c"
   mkdir "Android"
   chmod 755 *
fi
}


echo -e "${R}     Senthil360 LINUX SETUP script      ${N}"
echo ""
echo "=========================================="
echo ""
echo -e "${B}1.${N} s777 to bin "
echo ""
echo -e "${B}2.${N} Add alias to bashrc"
echo ""
echo -e "${B}3.${N} Clone gt_python"
echo ""
echo -e "${B}4.${N} Clone PythonML"
echo ""
echo -e "${B}0 -${N} Execute all the above"
echo ""
echo "------------------------------------------"
echo ""
echo -e "${G}Choose your option : ${N}"
echo ""

while true; do
   case $option in
      1)
        func_s777
        ;;
      2)
        perm_alias
        ;;
      3)
        setupGtPython
        ;;
      4)
        setupPythonML
        ;;
      0)
        func_s777
        perm_alias
        setupCodesDir
        setupGtPython
        setupPythonML
        ;;
      *)
        echo "Unknown option"
        ;;
   esac
done
      
