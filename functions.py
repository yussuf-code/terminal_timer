from time import sleep
from math import floor


def timer(time_in_seconds):
    
    while time_in_seconds:

        remaining_minutes = floor(time_in_seconds / 60)
        remaining_seconds = time_in_seconds % 60

        if remaining_minutes == 0:
            minutes = " Timer: 00"
        elif remaining_minutes < 10:
            minutes = f" Timer: 0{remaining_minutes}"
        elif remaining_minutes > 9:
            minutes = f" Timer: {remaining_minutes}"

        if remaining_seconds == 0:
            seconds = "00"
        elif remaining_seconds < 10:
            seconds = f"0{remaining_seconds}"
        elif remaining_seconds > 9:
            seconds = f"{remaining_seconds}"
        
        timer = f"{minutes}:{seconds}"
        print(f"{timer}", end="\r")

        sleep(1)
        time_in_seconds -= 1