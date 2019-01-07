import os


find = '\\'
if __file__.find("\\") == -1:
    find = '/'
    if __file__.find('/') == -1: 
        find = None
        rootdir = '.'

if find:
    l = __file__.rfind(find)
    rootdir = __file__[:l]+find+'..'+find+'framedata'+find+'skills'

skills = []
for root, subfolders, files in os.walk(rootdir):
    if root == rootdir :
        skills = subfolders

 #print skills
tmp = {}
for i in skills:
    if i.find(' ')== -1 :
        continue
    name,v = i.split(' ')
    tmp[name] = v.split('+')
skills = tmp
        
