import time
import os
from datetime import datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        now = datetime.now().strftime("%H:%M:%S")

        if now == alarm_time:
            print("⏰ ALARM! WAKE UP!")
            
            # Beep sound (Windows)
            try:
                import winsound
                winsound.Beep(1000, 1000)
            except:
                # Fallback for Mac/Linux
                print("\a")

            break

        time.sleep(1)

# Input format: HH:MM:SS (24-hour format)
alarm_time = input("Enter alarm time (HH:MM:SS): ")
set_alarm(alarm_time)
