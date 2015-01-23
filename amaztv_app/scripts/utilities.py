from datetime import datetime

def better_time_format(time):
    date_time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
    return date_time.strftime('%b, %d %Y - %H:%M')