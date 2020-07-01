import os

hosts = ['10.0.0.1', '10.0.0.2', 'google.com']
report = []

for host in hosts:
    response = os.system(f'ping -c 1 {host}')

    if response == 0:
        report.append([f'{host} is up!', 1])
    else:
        report.append([f'{host} is down!', 0])

print('-' * 40)

print('These hosts are down:')
for result in report:
    if result[1] == 0:
        print(f'\t {result[0]}')

print('-' * 40)

print('These hosts are up:')
for result in report:
    if result[1] == 1:
        print(f'\t {result[0]}')