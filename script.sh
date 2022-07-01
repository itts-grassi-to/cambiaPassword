#!/bin/bash
#tm="'$1 $2'"

#sudo smbpassword -x gigi
echo -e "$1\n$2" | sudo smbpasswd -a $3
#echo $tm
