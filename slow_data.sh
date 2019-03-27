#!/bin/bash
time=$1
if [ -z $1 ]; then 
    time=180
fi
echo "create slow chart (${time}s)"
echo 'name,star,element,weapon,str,condition,comment,dps' > www/${1}/slow_data.csv
python adv/ex_dagger.py     $1 | tee -a www/slow_data.csv
python adv/ex_blade.py      $1 | tee -a www/slow_data.csv
python adv/ex_wand.py       $1 | tee -a www/slow_data.csv

python adv/ex_dagger.py     $1 | tee -a www/60/slow_data.csv
python adv/ex_blade.py      $1 | tee -a www/60/slow_data.csv
python adv/ex_wand.py       $1 | tee -a www/60/slow_data.csv

python adv/ex_dagger.py     $1 | tee -a www/90/slow_data.csv
python adv/ex_blade.py      $1 | tee -a www/90/slow_data.csv
python adv/ex_wand.py       $1 | tee -a www/90/slow_data.csv

python adv/addis.py -2      ${1} | tee -a www/${1}/slow_data.csv
python adv/ieyasu.py -2     ${1} | tee -a www/${1}/slow_data.csv
python adv/sinoa.py -2      ${1} | tee -a www/${1}/slow_data.csv
python adv/ezelith.py -2    ${1} | tee -a www/${1}/slow_data.csv
python adv/sazanka.py -2    ${1} | tee -a www/${1}/slow_data.csv
python adv/botan.py -2      ${1} | tee -a www/${1}/slow_data.csv


if [ -z $1 ]; then 
        time=90
        echo "create slow chart (${time}s)"
        echo 'name,star,element,weapon,str,condition,comment,dps' > www/${time}/slow_data.csv
        python adv/addis.py -2      ${time} | tee -a www/${time}/slow_data.csv
        python adv/ieyasu.py -2     ${time} | tee -a www/${time}/slow_data.csv
        python adv/sinoa.py -2      ${time} | tee -a www/${time}/slow_data.csv
        python adv/ezelith.py -2    ${time} | tee -a www/${time}/slow_data.csv
        python adv/sazanka.py -2    ${time} | tee -a www/${time}/slow_data.csv
        python adv/botan.py -2      ${time} | tee -a www/${time}/slow_data.csv
fi

if [ -z $1 ]; then 
        time=60
        echo "create slow chart (${time}s)"
        echo 'name,star,element,weapon,str,condition,comment,dps' > www/${time}/slow_data.csv
        python adv/addis.py -2      ${time} | tee -a www/${time}/slow_data.csv
        python adv/ieyasu.py -2     ${time} | tee -a www/${time}/slow_data.csv
        python adv/sinoa.py -2      ${time} | tee -a www/${time}/slow_data.csv
        python adv/ezelith.py -2    ${time} | tee -a www/${time}/slow_data.csv
        python adv/sazanka.py -2    ${time} | tee -a www/${time}/slow_data.csv
        python adv/botan.py -2      ${time} | tee -a www/${time}/slow_data.csv
fi
