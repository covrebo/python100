from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    datetime_list = []
    loglines_split = (str.split(line))
    datetime_list.append(loglines_split[1][0:4])
    datetime_list.append(loglines_split[1][5:7])
    datetime_list.append(loglines_split[1][8:10])
    datetime_list.append(loglines_split[1][11:13])
    datetime_list.append(loglines_split[1][14:16])
    datetime_list.append(loglines_split[1][17:19])
    return datetime(int(datetime_list[0]), int(datetime_list[1]), int(datetime_list[2]),
             int(datetime_list[3]), int(datetime_list[4]), int(datetime_list[5]))


def time_between_shutdowns(loglines):
    shutdown_events = []
    for line in loglines:
        loglines_split = line.split(" ", 3)
        if loglines_split[3] == 'Shutdown initiated.\n':
            # print('event')
            shutdown_list = []
            shutdown_list.append(loglines_split[1][0:4])
            shutdown_list.append(loglines_split[1][5:7])
            shutdown_list.append(loglines_split[1][8:10])
            shutdown_list.append(loglines_split[1][11:13])
            shutdown_list.append(loglines_split[1][14:16])
            shutdown_list.append(loglines_split[1][17:19])
            shutdown_events.append(datetime(int(shutdown_list[0]), int(shutdown_list[1]),
                                            int(shutdown_list[2]), int(shutdown_list[3]),
                                            int(shutdown_list[4]), int(shutdown_list[5])))
    return(shutdown_events[1] - shutdown_events[0])