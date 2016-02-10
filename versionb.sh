#!/bin/bash 
File_name=$1
today=”(date +%Y-%m-%d)" 
f=$File_name
g=${f%.*}
myFile="$g"_"$today"
echo $myFile
cp $File_name $myFile
rename "s/$myFile/$myFile/"*.txt
