#!/bin/bash
#python deploy.py adv.py
#python deploy.py adv.py.sp.py -sp
python deploy.py veronica.py
python deploy.py cassandra.py
python deploy.py natalie.py
python deploy.py veronica.py.1hp.py -sp
python deploy.py natalie.py.1hp.py -sp
python deploy.py -c