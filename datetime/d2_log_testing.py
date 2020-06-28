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

# # For problem 1
# for line in loglines:
#     datetime_list = []
#     loglines_split = line.split(" ", 3)
#     datetime_list.append(loglines_split[1][0:4])
#     datetime_list.append(loglines_split[1][5:7])
#     datetime_list.append(loglines_split[1][8:10])
#     datetime_list.append(loglines_split[1][11:13])
#     datetime_list.append(loglines_split[1][14:16])
#     datetime_list.append(loglines_split[1][17:19])
#     print(line)
#     print(loglines_split)
#     # return datetime(int(datetime_list[0]), int(datetime_list[1]), int(datetime_list[2]),
#     #          int(datetime_list[3]), int(datetime_list[4]), int(datetime_list[5]))

# For problem 2
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
print(shutdown_events)
print(shutdown_events[1] - shutdown_events[0])
    # print(line)
    # print(loglines_split[3])
    # return datetime(int(datetime_list[0]), int(datetime_list[1]), int(datetime_list[2]),
    #          int(datetime
# for you to code:

# def convert_to_datetime(line):
#     """TODO 1:
#        Extract timestamp from logline and convert it to a datetime object.
#        For example calling the function with:
#        INFO 2014-07-03T23:27:51 supybot Shutdown complete.
#        returns:
#        datetime(2014, 7, 3, 23, 27, 51)
#     """
#     pass
#
#
# def time_between_shutdowns(loglines):
#     """TODO 2:
#        Extract shutdown events ("Shutdown initiated") from loglines and
#        calculate the timedelta between the first and last one.
#        Return this datetime.timedelta object.
#     """
#     pass