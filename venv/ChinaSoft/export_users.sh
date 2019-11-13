#!/usr/bin/env bash

if [ $2 -ge 999999 ]
then
        sleep 15
else
        sleep 3
fi
row_num=` wc -l $1 | awk -F " " '{print $1}'`
while (( $2 != $row_num ))
do
        row_num=` wc -l $1 | awk -F " " '{print $1}'`
done
cat $1 | awk -F "," '{print $1}' | sed -n 'p' >> $3.csv
res=` wc -l $3.csv | awk -F " " '{print $1}'`
echo "$3.csv 中的客户数量为：$res"