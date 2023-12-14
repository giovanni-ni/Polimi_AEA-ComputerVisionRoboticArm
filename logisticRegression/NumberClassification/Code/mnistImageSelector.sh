#!/bin/bash
<< 'MULTILINE-COMMENT'
input: 
    - path to mnist archive directory
    - path to output directory
    - digit "X Y Z" you want to extract
    - quantity of "N" images you want to extract (the same for every digit)

output: 
    - create a different directory for every digit "x", "Y", "Z" 
    - in each directory copies "N" images for each selected digit
MULTILINE-COMMENT

# read input data
read -p "mnist archive directory: " IN_DIR
#IN_DIR="../MNIST_complete/trainingSet/trainingSet"
read -p "output directory: " OUT_DIR
#OUT_DIR='../Dataset/ternary_mnist'


digits=(0 0 0 0 0 0 0 0 0 0)
echo what digits you want to extract?
echo to stop type "111"
read -p "> " digit
while [[ $digit -ne 111 ]]
    do 
        if [ $digit -ge 0 -a $digit -le 9 ]
        then
            digits[$digit]=1
        fi
    read -p "> " digit
done

read -p "how many images per digits? " n
n=$(($n+1))
for i in "${!digits[@]}"
do
    if [ $[digits[i]] -eq 1 ]
    then
        j=1
        mkdir $OUT_DIR/$i
        for filename in $IN_DIR/$i/*
        do 
            cp $filename $OUT_DIR/$i/$j.jpg
            j=$(($j+1))
            if [ $j -eq $n ]
            then
                break
            fi
        done   
    fi
done