#from core.log import *
import sys
from core.timeline import now
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
    return s, do_act_list

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

    line += "def do_act_list(self, e):\n"

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

class Acl_Action:
    INDENT = '    '
    PREP = """    try:
        {act} = self.{act}
    except Exception:
        raise AttributeError('{act} is not an action')"""
    ACT = """{indent}if {act}{args}:
{indent}    return '{act}'"""
    NONE = '{indent}return 0'
    QUEUE_ACT = """{indent}self.acl_queue.append(({act}, compile('{cond}', '<string>', 'eval')))"""
    dragon_act = re.compile(r'dragon(form)?.act\(([A-Za-z "\'\*\+\d]+)\)')
    def __init__(self, action):
        self.arguments = '()'
        if action.upper() == 'NONE':
            self.action = None
        elif action.startswith('dragon'):
            self.action = 'dragonform'
            res = self.dragon_act.match(action)
            if res:
                self.action = 'dragonform'
                self.arguments = '.act({})'.format(res.group(2))
        else:
            self.action = action
        self.depth = 0

    def prepare(self):
        if self.action is None:
            return False
        return self.PREP.format(act=self.action)

    def act(self):
        if self.action is None:
            return self.NONE.format(indent=self.INDENT*self.depth)
        return self.ACT.format(act=self.action, args=self.arguments, indent=self.INDENT*self.depth)

    def queue_act(self, cond, depth_mod=0):
        if self.action is None:
            raise ValueError('No actions queued')
        return self.QUEUE_ACT.format(act=self.action, args=self.arguments, cond=cond, indent=self.INDENT*(self.depth+depth_mod))

class Acl_Condition:
    INDENT = '    '
    IF = """{indent}if {cond}:
{block}"""
    ELIF = """{indent}elif {cond}:
{block}"""
    ELSE = """{indent}else:
{block}"""
    QUEUE = """{indent}if len(self.acl_queue)==0 and {cond}:
{block}"""
    banned = re.compile(r'(exec|eval|compile|setattr|delattr|memoryview|property|globals|locals|open|print|__[a-zA-Z]+__).*')
    banned_repl = 'True'
    assignment = re.compile(r'([^=><!])=([^=])')
    assignment_repl = lambda s: s[1]+'=='+s[2]
    @staticmethod
    def sanitize_qwe_and_his_chunch_legs(condition):
        condition = Acl_Condition.banned.sub(Acl_Condition.banned_repl, condition)
        condition = Acl_Condition.assignment.sub(Acl_Condition.assignment_repl, condition)
        return condition

    def __init__(self, condition, depth=0):
        self.conditions = [(self.sanitize_qwe_and_his_chunch_legs(condition), [])]
        self.depth = depth

    def add_action(self, action):
        action.depth = self.depth + 1
        self.conditions[-1][-1].append(action)

    def add_condition(self, condition):
        self.conditions.append((self.sanitize_qwe_and_his_chunch_legs(condition), []))

    def prepare(self):
        prep_list = []
        for _, acts in self.conditions:
            prep_list.extend([a.prepare() for a in acts if a.prepare()])
        return '\n'.join(prep_list)

    def act(self):
        act_list = []
        for idx, value in enumerate(self.conditions):
            cond, acts = value
            if len(acts) == 0:
                continue
            if cond.startswith('QUEUE'):
                cond = 'True' if len(cond) < 6 else cond[6:]
                pattern = self.QUEUE
                block = [a.queue_act('True') for a in acts]
                block.append("{indent}    return 'queued'".format(indent=self.INDENT*self.depth))
            else:
                if idx == 0:
                    pattern = self.IF
                elif cond != 'ELSE':
                    pattern = self.ELIF
                else:
                    pattern = self.ELSE
                block = [a.act() for a in acts]
            if self.depth == 0:
                act_list = block
            else:
                act_list.append(
                    pattern.format(cond=cond, block='\n'.join(block), indent=self.INDENT*self.depth)
                )
        return '\n'.join(act_list)

    def queue_act(self, bolb):
        act_list = []
        for value in self.conditions:
            cond, acts = value
            if len(acts) == 0:
                continue
            act_list = [a.queue_act(cond, depth_mod=-1) for a in acts]
        return '\n'.join(act_list)

def acl_str(acl):
    acl_base = """
def do_act_list(self, e):
    this = self
    pin, dname, dstat, didx = e.pin, e.dname, e.dstat, e.didx
    prev = self.action.getprev()
    seq = didx if dname[0] == 'x' else 0 if dstat == -2 else -1
    cancel = pin =='x' or pin == 'fs'
    x = didx if pin =='x' else 0
    fsc = pin =='fs'
    s = int(pin[1]) if (pin[0] == 's' and pin[1] in ('1', '2', '3')) or pin[-2:] == '-x' else 0
    sp = dname if pin == 'sp' else 0
    prep = pin == 'prep'
    sim_duration = self.duration
{act_prep_block}
    if len(self.acl_queue) > 0:
        next_act, next_cond = self.acl_queue[0]
        if eval(next_cond) and next_act():
            self.acl_queue.pop(0)
        return 'queue'
{act_cond_block}
    return 0"""
    root = Acl_Condition('True')
    node_stack = [root]
    real_lines = []
    for line in acl.split('\n'):
        line = line.strip().replace('`', '')
        if len(line) > 0 and line[0] != '#':
            if ';' in line:
                for s in line.split(';'):
                    s = s.strip().replace('`', '')
                    if len(s) > 0 and s[0] != '#':
                        real_lines.append(s)
            else:
                real_lines.append(line)
    for line in real_lines:
        upper = line.upper()
        if upper.startswith('IF '):
            node = Acl_Condition(line[3:])
            node_stack[-1].add_action(node)
            node_stack.append(node)
        elif upper.startswith('QUEUE'):
            node = Acl_Condition('QUEUE'+line[5:])
            node_stack[-1].add_action(node)
            node_stack.append(node)
        elif upper.startswith('ELIF '):
            node_stack[-1].add_condition(line[5:])
        elif upper.startswith('ELSE'):
            node_stack[-1].add_condition('ELSE')
        elif upper.startswith('END'):
            node_stack.pop()
        else:
            parts = [l.strip() for l in line.split(',')]
            if len(parts) == 1 or len(parts[1]) == 0:
                action = parts[0]
                node = Acl_Action(action)
                node_stack[-1].add_action(node)
            else:
                action = parts[0]
                condition = parts[1]
                node = Acl_Condition(condition)
                node_stack[-1].add_action(node)
                node.add_action(Acl_Action(action))
    acl_string = acl_base.format(
        act_prep_block=root.prepare(),
        act_cond_block=root.act()
    )
    return acl_string