#!/bin/bash
echo "============================"
echo "create data chart (sp)"
echo '----------------------------'
cp www/sp/slow_data.csv www/sp/data.csv
python adv/xander.py.best.py       -2  | tee -a www/sp/data.csv
python adv/vanessa.py.void.py      -2  | tee -a www/sp/data.csv
python adv/heinwald.py             -2  | tee -a www/sp/data.csv
python adv/linyou.py.z.py          -2  | tee -a www/sp/data.csv
python adv/louise.py.doublebuff.py -2  | tee -a www/sp/data.csv
python adv/veronica.py.1hp.py      -2  | tee -a www/sp/data.csv
python adv/marth.py.cheese.py      -2  | tee -a www/sp/data.csv
python adv/elisanne.py.goodteam.py -2  | tee -a www/sp/data.csv
python adv/melody.py.goodteam.py   -2  | tee -a www/sp/data.csv
python adv/g_mym.py.sp.py          -2  | tee -a www/sp/data.csv
