import core.timeline
import sys

class Log(list):
    def log(self, *args):
        self.append([core.timeline.now(), *args])

    def filter_iter(self, log_filter):
        filter_idx, filter_value = log_filter
        for entry in self:
            try:
                if entry[filter_idx] == filter_value:
                    yield entry
            except:
                continue

    def write_logs(self, log_filter=None, fn=None):
        if fn is None:
            fn = sys.stdout
        if log_filter is None:
            log_iter = self
        else:
            log_iter = self.filter_iter(log_filter)
        for entry in log_iter:
            time = entry[0]
            fn.write('{:>8.3f}: '.format(time))
            for value in entry[1:]:
                if isinstance(value, float):
                    fn.write('{:<8.3f}'.format(value))
                else:
                    fn.write('{:<16},'.format(value))
            fn.write('\n')

    def get_log_list(self):
        return list(self)

loglevel = 0

g_logs = Log()
log = g_logs.log
logcat = g_logs.write_logs
logget = g_logs.get_log_list
logreset = g_logs.clear