# tools.py
from db import add_event, get_events

def check_conflict(date, time):
    events = get_events()
    for e in events:
        if e[2] == date and e[3] == time:
            return True
    return False

def schedule_event(title, date, time):
    if check_conflict(date, time):
        return "Conflict detected! Try another time."
    
    add_event(title, date, time)
    return f"Event '{title}' scheduled on {date} at {time}"