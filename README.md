One night, my phone broke and I realized I had school the next morning. to make sure I woke up on time,
i built a simple alarm system using a Raspberry Pi, a breadboard, a passive buzzer module, jumper wires, and a resistor. I designed the circuit, connected it to the Raspberry Pi’s GPIO pins, and wrote a Python script to trigger the buzzer at a set time. The project worked successfully and woke me up the next morning.

Here's a step by step how i made the alarm work: 

Step 1: Connect the Raspberry Pi to a monitor and power it on.

Step 2: set up the breadboard and wire the passive buzzer module to the GPIO pins:

OConnect the positive pin of the buzzer to GPIO 18

Connect the negative pin of the buzzer to GPIO 6 

<img src="GPIOPINS.png" width="500">

Step 3: Write a Python script (alarm_clock.py) to control the GPIO pins and trigger the buzzer at a scheduled time. Save the script in a folder

Step 4: Open the command-line interface (CLI), navigate to the script folder:

cd /path/to/raspberrypiscripts
ls

Verify the Python script is present, then run:

python3 alarm_clock.py

The buzzer will sound at the scheduled time, successfully functioning as an alarm 
If you're using a different GPIO pin as shown as above, you need to change the parameters in the python code to match it.
