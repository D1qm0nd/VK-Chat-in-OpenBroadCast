import json

class Logger:
    def log(self, logpath, log, operation='w+'):
        try:
            with open(logpath, operation) as logsf:
                json.dump(log, logsf, indent=4)
                logsf.close()
            return True
        except:
            return False