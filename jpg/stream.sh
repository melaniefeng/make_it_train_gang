#!/bin/zsh

cd data
num=0
while true
do 
    echo "getting photo ..."
    wget -q -O $num.jpg http://10.147.244.66:8000/shot.jpg
    num=$((num+1)) 
    sleep 0.1 
done
