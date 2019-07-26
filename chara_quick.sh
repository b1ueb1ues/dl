#!/bin/bash

time=$1
if [ -z $1 ]; then 
    time='180'
fi
prefix=$time
if [ $prefix = '180' ]; then 
    prefix=''
fi
echo "
============================"
echo "create data chart (${time}s)"
echo '----------------------------'
cp www/${prefix}/slow_data_${2}.csv www/${prefix}/data_${2}.csv
python adv/berserker.py -2   ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/euden.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/karl.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/naveed.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/raemond.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/rodrigo.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/xander.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/zardin.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/aoi.py -2         ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/celliera.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/h_edward.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/jurota.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/melody.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/mikoto.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/musashi.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/taro.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/althemia.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/amane.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/d_xander.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/kleimann.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/lily.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/lucretia.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/maribelle.py -2   ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/nicolas.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/xania.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/d_cleo.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/francesca.py -2   ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/irfan.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/luther.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/melsa.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/orion.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/orsem.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/renelle.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/vida.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/vice.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/erik.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/johanna.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/julietta.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/karina.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/linus.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/pietro.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/ranzal.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/rex.py -2         ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/vanessa.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/aeleen.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/alain.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/cibella.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/elisanne.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/h_elisanne.py -2  ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/malka.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/pia.py -2         ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/ryozen.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/xainfried.py -2   ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/zace.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/d_nefaria.py -2   ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/eleonora.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/elias.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/hawk.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/joe.py -2         ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/louise.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/luca.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/malora.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/nefaria.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/philia.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/rawn.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/waike.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/g_sarisse.py -2   ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/annelie.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/marty.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/fritz.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/linyou.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/kuhai.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/xiaolei.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/sufang.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/v_ezelith.py -2   ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/v_orion.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/albert.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/odetta.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/jakob.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/curran.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/g_ranzal.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/laranoa.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/fleur.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/yue.py -2         ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/sylas.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/alex.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/alfonse.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/marth.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/veronica.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/fjorm.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/b_zardin.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/norwin.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/yachiyo.py -2     ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/g_mym.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/serena.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/s_maribelle.py -2 ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/xuanzang.py -2    ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/w_elisanne.py -2  ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/w_aoi.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/yaten.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/ramona.py -2      ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/rena.py -2        ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
python adv/renee.py -2       ${time} ${2} | tee -a www/${prefix}/data_${2}.csv
