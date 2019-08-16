from core import Conf

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


    csvconf = {}
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
                csvconf[title[i]] = r
                i+=1

    if csvconf['s1_buff'] != '' and csvconf['s1_buff']!= '0':
        tmp = csvconf['s1_buff'].split(';')
        csvconf['s1_buff'] = []
        if len(tmp) >= 3 :
            csvconf['s1_buff'] = [ tmp[0],float(tmp[1]), float(tmp[2]) ]
            for i in tmp[3:]:
                csvconf['s1_buff'] += [i]
        elif len(tmp) == 2:
            csvconf['s1_buff'] = [ 'none',float(tmp[0]), float(tmp[1]) ]
    else:
        csvconf.pop('s1_buff')

    if csvconf['s2_buff'] != '' and csvconf['s2_buff']!= '0':
        tmp = csvconf['s2_buff'].split(';')
        csvconf['s2_buff'] = []
        if len(tmp) >= 3 :
            csvconf['s2_buff'] = [ tmp[0],float(tmp[1]), float(tmp[2]) ]
            for i in tmp[3:]:
                csvconf['s2_buff'] += [i]
        elif len(tmp) == 2:
            csvconf['s2_buff'] = [ 'none',float(tmp[0]), float(tmp[1]) ]
    else:
        csvconf.pop('s2_buff')

    conf = Conf()

    conf.s1.dmg = float(csvconf['s1_dmgpc'])/100.0
    conf.s1.sp = int(csvconf['s1_sp'])
    conf.s1.buff = csvconf['s1_buff'] if 's1_buff' in csvconf else None

    conf.s2.dmg = float(csvconf['s2_dmgpc'])/100.0
    conf.s2.sp = int(csvconf['s2_sp'])
    conf.s2.buff = csvconf['s2_buff'] if 's2_buff' in csvconf else None

    conf.c.att = int(csvconf['str_adv'])
    conf.c.ele = csvconf['element']
    conf.c.wt = csvconf['weapon']
    conf.c.stars = csvconf['stars']

    return conf
    

if __name__ == "__main__":
    get('xander')

