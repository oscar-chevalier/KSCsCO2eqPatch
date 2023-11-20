#!/bin/bash

separate_args()
{
    IFS='@'
    read -a strarr <<< "$infos"

    category="${strarr[0]}"
    namefile="${strarr[1]}"
    price="${strarr[2]}"
    path="${strarr[3]}"
}

modify_price() 
{
    separate_args "$1"
    # price="$price"
    echo "path $path"
    sed -iE "s/cost = .*$/cost = $price/" "$path"
} 

if [ "$1" = "-c" ]; then
    echo "COPYING the files"
    cp -r -v 'ksp' 'Kerbal Space Program'
    echo "COPYING finished"
fi

while read line ; do
    # lexe line
    echo "line $line"
    infos=$(echo "$line" | sed -nE 's/([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]+)/\1@\4@\5@\9/p')
    echo "infos $infos"
    if [ "$infos" = "" ]; then
        echo IGNORED "$line"
    else
        modify_price "$infos"
    fi
done < parts_to_insert.csv

find 'Kerbal Space Program' '-name' '*.cfgE' '-delete'
