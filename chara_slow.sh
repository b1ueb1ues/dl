#!/bin/bash
time=$1
if [ -z $1 ]; then 
    time=180
fi
echo 'dps,name,star,element,weapon,str,condition,amulets,comment' > www/${1}/slow_data.csv

echo "create ex chart (${time}s)"
python adv/ex_dagger.py     $1 | tee -a www/${1}/slow_data.csv
python adv/ex_blade.py      $1 | tee -a www/${1}/slow_data.csv
python adv/ex_wand.py       $1 | tee -a www/${1}/slow_data.csv

echo "create slow chart (${time}s)"

python adv/addis.py -2      ${1} | tee -a www/${1}/slow_data.csv
python adv/ieyasu.py -2     ${1} | tee -a www/${1}/slow_data.csv
python adv/sinoa.py -2      ${1} | tee -a www/${1}/slow_data.csv
python adv/ezelith.py -2    ${1} | tee -a www/${1}/slow_data.csv
python adv/sazanka.py -2    ${1} | tee -a www/${1}/slow_data.csv
python adv/botan.py -2      ${1} | tee -a www/${1}/slow_data.csv
