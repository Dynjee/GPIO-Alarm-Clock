from gpiozero import Buzzer
from time import sleep
from datetime import datetime

# Set buzzer pin (GPIO 18)
buzzer = Buzzer(18)

# Set your alarm time (24-hour format)
ALARM_HOUR = 7
ALARM_MINUTE = 0

def buzz(duration=10):
    """Buzz on and off for a duration (seconds)"""
    end_time = duration
    while end_time > 0:
        buzzer.on()
        sleep(0.2)
        buzzer.off()
        sleep(0.2)
        end_time -= 0.4

print("Alarm is set...")

try:
    while True:
        now = datetime.now()

        if now.hour == ALARM_HOUR and now.minute == ALARM_MINUTE:
            print("Wake up! Alarm triggered.")
            buzz(10)
            break

        sleep(10)

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    buzzer.off()
