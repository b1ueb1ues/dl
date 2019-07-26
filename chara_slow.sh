#!/bin/bash
time=$1
if [ -z $1 ]; then 
    time='180'
fi
prefix=$time
if [ $prefix = '180' ]; then 
    prefix=''
fi

echo 'dps,name,star,element,weapon,str,amulets,condition,comment,' > www/${prefix}/slow_data_${2}.csv

#echo "create ex chart (${time}s)"
#python adv/ex_dagger.py     $1 | tee -a www/${1}/slow_data.csv
#python adv/ex_blade.py      $1 | tee -a www/${1}/slow_data.csv
#python adv/ex_wand.py       $1 | tee -a www/${1}/slow_data.csv

echo "create slow chart (${time}s)"

python adv/addis.py -2      ${time} ${2} | tee -a www/${prefix}/slow_data_${2}.csv
python adv/ieyasu.py -2     ${time} ${2} | tee -a www/${prefix}/slow_data_${2}.csv
python adv/sinoa.py -2      ${time} ${2} | tee -a www/${prefix}/slow_data_${2}.csv
python adv/ezelith.py -2    ${time} ${2} | tee -a www/${prefix}/slow_data_${2}.csv
python adv/sazanka.py -2    ${time} ${2} | tee -a www/${prefix}/slow_data_${2}.csv
python adv/botan.py -2      ${time} ${2} | tee -a www/${prefix}/slow_data_${2}.csv
python adv/natalie.py -2    ${time} ${2} | tee -a www/${prefix}/slow_data_${2}.csv
