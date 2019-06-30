#!/bin/bash
echo "============================"
echo 'create slow data chart (sp)'
echo '----------------------------'
echo 'dps,name,star,element,weapon,str,amulets,condition,comment' > www/sp/slow_data.csv
python adv/addis.py.hmcmeta.py -2 | tee -a www/sp/slow_data.csv
python adv/natalie.py.hp1.py   -2 | tee -a www/sp/slow_data.csv

