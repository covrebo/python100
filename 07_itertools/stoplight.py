import sys
import itertools
import time
import random

light_cycle = itertools.cycle(['Green', 'Yellow', 'Red'])
next_light = next(light_cycle)
light_length = list(range(5, 10))


while True:
    sys.stdout.write('\r' + next_light)
    next_light = next(light_cycle)
    sys.stdout.flush()
    if next_light == 'Yellow' or next_light == 'Green':
        time.sleep(random.choice(light_length))
    else:
        time.sleep(2)