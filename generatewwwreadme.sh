#!/bin/sh 
cp wwwREADME.md www/README.md
python markdown2.py www/README.md > www/readme.html 2>&1
