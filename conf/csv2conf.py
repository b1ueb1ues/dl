
def get(mname):
    csvname = ''
    find = '/'
    if __file__.find('/') == -1:
        find = '\\'
        if __file__.find('\\') == -1:
            find = None
            csvname = 'adv_data.csv'
    if find:
        l = __file__.rfind(find)
        csvname = __file__[:l] + find + 'adv_data.csv'


    conf = {}
    f = open(csvname,'r')
    title = f.readline().strip().split(',')

    #find name
    idx = title.index('name')
    mname = mname.lower()
    for line in f:
        row = line.strip().split(',')
        if row[idx].lower() == mname:
            i = 0
            for r in row:
                conf[title[i]] = r
                i+=1
    conf['s1_dmg'] = int(conf['s1_dmgpc'])/100.0
    conf['s2_dmg'] = int(conf['s2_dmgpc'])/100.0
    conf['s1_sp'] = int(conf['s1_sp'])
    conf['s2_sp'] = int(conf['s2_sp'])
    conf['str_adv'] = int(conf['str_adv'])
    if conf['s1_buff'] != '' and conf['s1_buff']!= '0':
        tmp = conf['s1_buff'].split(';')
        conf['s1_buff'] = [ float(tmp[0]), float(tmp[1]), tmp[2] ]
    if conf['s2_buff'] != '' and conf['s2_buff']!= '0':
        tmp = conf['s2_buff'].split(';')
        conf['s2_buff'] = [ float(tmp[0]), float(tmp[1]), tmp[2] ]
    return conf
    

if __name__ == "__main__":
    get('xander')

