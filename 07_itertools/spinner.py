import sys
import itertools
import time

sympbols = itertools.cycle('\|/-')

while True:
    sys.stdout.write('\r' + next(sympbols))
    sys.stdout.flush()
    time.sleep(0.1)