#from core.log import *
import sys
from core.timeline import now
from adv.adv_test import sim_duration
import imp
import re

g_line = ""

do_act = None

def acl_func_str(acl):
    global do_act
    s = acl_str(acl)
    exec(s,globals())
    # return do_act_list, s
    do_act = do_act_list
    return s

# def acl_func(acl):
#     s = acl_str(acl)
#     exec(s,globals())
#     return do_act_list

def acl_str_but_it_cursed(acl):
    global g_line
    aif = []
    aif_list = []
    prepare_list = []


    aifline = -1
    prepareline = -1
    curr = 'none'
    for i in acl:
        if i == "`":
            aifline += 1
            aif.append("")
            curr = 'aif'
        elif i == "#":
            prepareline += 1
            prepare_list.append("")
            curr = 'prepare'
        else:
            if curr == 'aif':
                aif[aifline] += i
            elif curr == 'prepare':
                prepare_list[prepareline] += i

    for i in aif:
        aif_list.append( i.split(',', 1) )

    line = ""

    line += "def do_act_list(this, e):\n"

    for i in prepare_list:
        line += "    %s\n"%(i.strip().replace('\n','\n    '))

    for i in aif_list:
        if len(i) == 1:
            line += "    if %s():\n"%( i[0].strip() )
            line += "        return '%s'\n"%( i[0].strip() )
            #line_list.append("%s()\n"%i[0])
        elif len(i) == 2:
            condi = i[1].strip().replace("=","==")
            condi = condi.replace("====","==")
            condi = condi.replace("!==","!=")
            condi = condi.replace(">==",">=")
            condi = condi.replace("<==","<=")
            #condi = i[1].strip()
            line += "    if %s :\n"%( condi )
            line += "        if %s():\n"%( i[0].strip() )
            line += "            return '%s'\n"%( i[0].strip() )
            #line_list.append( "if %s :\n    %s()\n"%(i[1],i[0]) )

    line += '    return 0'
    #g_line = line
    return line


def eq_replace(s):
    return s[1]+'=='+s[2]

def acl_str(acl):
    act_cond_list = []

    for line in acl.split('\n'):
        line = line.strip()
        if len(line) > 0 and line[0] == '`':
            parts = [l.strip() for l in line[1:].split(',')]
            try:
                act_cond_list.append((parts[0], parts[1] if len(parts[1]) > 0 else None))
            except:
                act_cond_list.append((parts[0], None))
    
    acl_base = """
def do_act_list(this, e):
    pin, dname, dstat, didx = e.pin, e.dname, e.dstat, e.didx
    prev = this.action.getprev()
    seq = didx if dname[0] == 'x' else 0 if dstat == -2 else -1
    cancel = pin =='x' or pin == 'fs'
    x = didx if pin =='x' else 0
    fsc = pin =='fs'
    s = int(pin[1]) if (pin[0] == 's' and pin[1] != 'p') or pin[-2:] == '-x' else 0
    sp = dname if pin == 'sp' else 0
    prep = pin == 'prep'
{act_prep_block}
{act_cond_block}
    return 0"""
    acl_prep = """    try:
        {act} = this.{act}
    except Exception:
        raise AttributeError('{act} is not an action')"""
    acl_if_no_cond = """    if {act}{args}:
        return '{act}'"""
    acl_if_cond = """    if {cond}:
        if {act}{args}:
            return \'{act}\'"""
    act_prep_block = []
    act_cond_block = []
    for act, cond in act_cond_list:
        if act.startswith('dragon'):
            act_prep_block.append(acl_prep.format(act='dragonform'))
            if act.startswith('dragon.act'):
                args = act.replace('dragon', '')
            else:
                args = '()'
            act = 'dragonform'
        else:
            act_prep_block.append(acl_prep.format(act=act))
            args = '()'
        if cond is None:
            act_cond_block.append(acl_if_no_cond.format(act=act, args=args))
        else:
            cond = re.sub(r'([^=><!])=([^=])', eq_replace, cond)
            act_cond_block.append(acl_if_cond.format(cond=cond, act=act, args=args))
    acl_string = acl_base.format(act_prep_block='\n'.join(act_prep_block),act_cond_block='\n'.join(act_cond_block))
    return acl_string