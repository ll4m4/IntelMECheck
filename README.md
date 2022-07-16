# IntelMECheck
Checks if Intel Management Engine is running on a Windows system with glitched
IME firmware that doesn't always load. The script reboots until it detects
the IME driver has loaded. Otherwise if IME isn't running the system will
instantly power off 30 minutes after the machine was powered on.

I had to use wavs due to TTS not outputting sound when the script is run
in the background.

The script needs to be added to task scheduler.

Security options: Run whether user is logged in or not.

Trigger: At System Startup

Action: Start a program: \<full path to python executable\> \<full path to IntelMECheck.py\>

eg: c:\Users\someuser\AppData\Local\Programs\Python\Python310\python.exe c:\wherever\IntelMECheck.py
