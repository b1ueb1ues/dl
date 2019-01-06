import os

rootdir = "framedata/skills"
skills = []

for root, subfolders, files in os.walk(rootdir):
    if root == rootdir :
        skills = subfolders

 #print skills
tmp = {}
for i in skills:
    name,v = i.split(' ')
    tmp[name] = v.split('+')
skills = tmp
        
