from datetime import datetime

start = input('Input Start to start the timer: ')
while str.lower(start) != 'start':
    start = input('Input Start to start the timer: ')
start = datetime.now()

stop = input('Input Stop to stop the timer: ')
while str.lower(stop) != 'stop':
    stop = input('Input Stop to stop the timer: ')
stop = datetime.now()

print(f'Your time is: {stop - start}')