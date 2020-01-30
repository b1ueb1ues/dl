#!/bin/bash
#python deploy.py adv.py
#python deploy.py adv.py.sp.py -sp
# these r people that need redeploy for flurry
python deploy.py delphi.py
python deploy.py d_cleo.py
python deploy.py g_sarisse.py
python deploy.py g_sarisse.py.rollfs.py -sp
python deploy.py laranoa.py
python deploy.py laranoa.py.rollfs.py -sp
python deploy.py s_cleo.py
python deploy.py v_ezelith.py
python deploy.py g_luca.py
python deploy.py g_luca.py -sp
# these r mh people
python deploy.py -c