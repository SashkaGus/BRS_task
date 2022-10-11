from time import time


def time_converter(time):
    from datetime import datetime
    dt = datetime.strptime(time, '%H:%M').strftime("%I:%M %p").lower()
    if dt.endswith('pm'):
        dt = dt.replace('pm', 'p.m.')
    else:
        dt = dt.replace('am', 'a.m.')
    return dt.strip('0')

print(time_converter('09:30'))