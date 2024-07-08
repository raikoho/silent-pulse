# 🦇 Silent Pulse: The Ultimate Stealth Monitoring Tool 🦇

> *"In the shadows, we find the truth."*

![DarkWatcher Banner](silentpulse.png)

## 🕵️‍♂️ What is Silent Pulse?
Silent Pulse - it is an optimized python script that aims to help real computer users detect any unwanted third-party activity on that computer.
This means that you will find out who, why and what was doing on your computer during your absence.

## ⚠️ Disclaimer
**WARNING:** This tool is intended for use on devices you own or have explicit permission to monitor. Unauthorized use of Silent Pulse can be illegal and unethical. By using this software, you agree to take full responsibility for your actions.

## ⚡ Features
- **Silent Monitoring:** Operates in the background without detection. 
- **Screenshot Capture:** Takes periodic screenshots to record on-screen activity.
- **Keylogger:** Add modules such as keylogger or other program.
- **Customizable Intervals:** Adjust the frequency of screenshots and keystroke logging.
- **Stealth Mode:** Disguises itself to avoid suspicion.

## 🛠️ Work algorithm and custom settings:
- Launch.
- Waiting time before activity tracking starts - 15 seconds.
- If there is no activity, the program does nothing.
- If the activity took place (keyboard or mouse), the 3 modules are activated:
 
      1) screenshot of the screen - every 15 seconds;
      2) webcam screenshot - every 1 minute;
      3) launch any additional program - in this case - a keylogger. You can add your own program or use my keylogger on GitHub.
  
**if you will use my Keylogger - be sure that its named as keylogger.py and stored exactly in the main directory.**
       
- If you press the keys "alt + space" at the same time, the program completely suspends its work and tracking algorithms.
- All data will be saved in the "output" folder, which is located in the directory with the script.

## 🎩 Installation

```bash
git clone https://github.com/raikoho/silent-pulse.git
cd silent-pulse
./silent-pulse.py
```

## 🧩 Dependencies
The script uses the following modules that you should install before running (if you don't already have them):

**cv2, pillow, pynput, subprocess**


