#
# IntelMECheck.py
# Checks if Intel Management Engine is running on a system with glitched
# IME firmware that doesn't always load. The script reboots until it detects
# the IME driver has loaded. Otherwise if IME isn't running the system will
# instantly power off 30 minutes after the machine was powered on.
#
# I had to use wavs due to TTS not outputting sound when the script is run
# in the background.
#
# The script needs to be added to task scheduler.
# Security options: Run whether user is logged in or not.
# Trigger: At System Startup
# Action: Start a program: <full path to python executable> <full path to IntelMECheck.py>
# eg: c:\Users\someuser\AppData\Local\Programs\Python\Python310\python.exe c:\wherever\IntelMECheck.py
#
# Last Updated: 7/15/22
#

import os
from win32com.client import GetObject
import winsound

source_file = os.path.dirname(os.path.abspath(__file__)) + "\\" # Get script source dir.
driver_name = "Intel(R) Management Engine Interface"

def is_driver_loaded(x):
    if x:
        winsound.PlaySound(source_file + "success.wav", winsound.SND_FILENAME)
        exit()
    else:
        winsound.PlaySound(source_file + "fail.wav", winsound.SND_FILENAME)
        os.system('shutdown /r /t 1') # Send reboot to Windows.

winsound.PlaySound(source_file + "init.wav", winsound.SND_FILENAME)
winsound.PlaySound(source_file + "search.wav", winsound.SND_FILENAME)

objWMI = GetObject('winmgmts:').InstancesOf('Win32_PnPSignedDriver') # Pull driver list.

for obj in objWMI: # Loop through and search for IME.
    if driver_name in str(obj.DeviceName):
        print(obj.DeviceName + "Running...")
        is_driver_loaded(True)

is_driver_loaded(False)
