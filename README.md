<p align=”center”>
<img width=”200" height=”200" src=”[https://github.com/raikoho/silent-pulse/assets/46958633/60bb6cfb-e834-4d6c-83c8-3df7e6a134bb](https://github.com/raikoho/silent-pulse/assets/46958633/ffc3e71e-776f-43de-a8fd-f7d92bc3c5f4)" alt=”my banner”>
</p>

Silent Pulse - it is an optimized python script that aims to help real computer users detect any unwanted third-party activity on that computer.
This means that you will find out who, why and what was doing on your computer during your absence.

Work algorithm and custom settings:
- Launch.
- Waiting time before activity tracking starts - 15 seconds.
- If there is no activity, the program does nothing.
- If the activity took place (keyboard or mouse), the following modules are activated:
    1) screenshot of the screen - every 15 seconds;
    2) webcam screenshot - every 1 minute;
    3) launch any additional program - in this case - a keylogger. You can add your own program or use my keylogger on GitHub.
       if you will use my Keylogger - be sure that its named as keylogger.py and stored exactly in the main directory.
       
- If you press the keys "alt + space" at the same time, the program completely suspends its work and tracking algorithms.
- All data will be saved in the "own" folder, which is located in the directory with the script.
