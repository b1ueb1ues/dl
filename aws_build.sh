#!/bin/bash
#python deploy.py adv.py
#python deploy.py adv.py.sp.py -sp
export COMMIT_MSG='update new shadow 70mc'
python deploy.py botan.py
python deploy.py cassandra.py
python deploy.py curran.py
python deploy.py curran.py.poison.py -sp
python deploy.py heinwald.py -sp
python deploy.py lathna.py
python deploy.py lathna.py.poison.py -sp
python deploy.py patia.py
python deploy.py -c