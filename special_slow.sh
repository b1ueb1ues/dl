#!/bin/bash
echo "============================"
echo 'create slow data chart (sp)'
echo '----------------------------'
echo 'name,star,element,weapon,str,condition,comment,dps' > www/sp/slow_data.csv
python adv/addis.py.haste.py -2 | tee -a www/sp/slow_data.csv

