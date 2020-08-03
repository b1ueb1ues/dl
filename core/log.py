import core.timeline
import sys

class Log:
    def __init__(self):
        self.reset()

    @staticmethod
    def update_dict(dict, name: str, value):
        try:
            dict[name] += value
        except KeyError:
            dict[name] = value

    def log(self, *args):
        time_now = core.timeline.now()
        self.record.append([time_now, *args])
        if len(args) >= 2:
            category = args[0]
            name = args[1]
            if category == 'dmg':
                if name[0:2] == 'o_' and name[2] in self.damage:
                    name = name[2:]
                if name[0] in self.damage:
                    self.update_dict(self.damage[name[0]], name, float(args[2]))
                else:
                    self.update_dict(self.damage['o'], name, float(args[2]))
            elif category == 'x' or category == 'cast':
                self.update_dict(self.counts[name[0]], name, 1)
                self.act_seq.append(name)
            elif category == 'buff' and name == 'team':
                if self.p_buff is not None:
                    pt, pb = self.p_buff
                    self.team_buff += (time_now - pt) * pb
                self.p_buff = (time_now, float(args[2]))
            elif category in ('energy', 'inspiration') and name == 'team':
                self.update_dict(self.team_tension, category, float(args[2]))

    def filter_iter(self, log_filter):
        for entry in self.record:
            try:
                if entry[1] in log_filter:
                    yield entry
            except:
                continue

    def write_logs(self, log_filter=None, output=None):
        if output is None:
            output = sys.stdout
        if log_filter is None:
            log_iter = self.record
        else:
            log_iter = self.filter_iter(log_filter)
        for entry in log_iter:
            time = entry[0]
            output.write('{:>8.3f}: '.format(time))
            for value in entry[1:]:
                if isinstance(value, float):
                    output.write('{:<8.3f}'.format(value))
                else:
                    output.write('{:<16},'.format(value))
            output.write('\n')

    def get_log_list(self):
        return self.record

    def reset(self):
        self.record = []
        self.damage = {'x':{},'s':{},'f':{},'d':{},'o':{}}
        self.counts = {'x':{},'s':{},'f':{},'d':{},'o':{}}
        self.p_buff = None
        self.team_buff = 0
        self.team_tension = {}
        self.act_seq = []

loglevel = 0

g_logs = Log()
log = g_logs.log
logcat = g_logs.write_logs
logget = g_logs.get_log_list
logreset = g_logs.reset