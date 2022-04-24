# elden-ring-bot
A bot to farm palace ledge with late game junk

## Installation

* python -m pip install requirements.txt

## Hold my hand instructions

* Download Visual Studio Code
* Create a projects folder (Documents/projects works)
* Open the terminal (ctrl + `)
* Install python if you don't already have it
* Type the installation command above
* As long as there were no errors then you can go to the Run Requirements and the Running section to get this working

## Installing with VirtualEnv

* Install python 382 https://www.python.org/downloads/release/python-382/
* pip install virtualenv
* py -3.8-32 -m virtualenv py3832
* .\py3832\Scripts\activate
* python -m pip install requirements.txt

## Run Requirements

* Elden Ring should be on your default screen / main monitor running in windowed mode
* No other windows should be overtop of Elden Ring
* Must be at the Palace Approach site of grace
* Must have the Sacred Relic sword and sufficient stats to clear mobs
* While the bot is running don't mouse the mouse or press anything

## Running

* Go to the Palace Approach Ledge-Road with fancy sword equipped
* Run `python main.py`

## Stopping

* Alt+tab to another window or click outside of Elden Ring and then the script should stop on its own because you're not in the Elden Ring window anymore

## TODO

* Determine if running forward and killing more mobs is worth it
* Cleanup autopy stuff or use it for reading images etc...

## Win32 notes / Troubleshooting

There are functions to set the active window but for some reason these aren't working. I've just set this bot to click into the window which it why it attacks on session start.

The keyboard events include a "MapVirtualKey" function which wasn't on most examples I saw online but it's the only method that seems to work here.

**Sample Functions**
* win32api.SetCursorPos((1000,1000))                            
* win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 1000, 1000, 0, 0)
* win32api.keybd_event(17, win32api.MapVirtualKey(17,0), 0, 0)
* time.sleep(0.5)
* win32api.keybd_event(17, win32api.MapVirtualKey(17,0), win32con.KEYEVENTF_KEYUP, 0)

If you have trouble with timings not working on your machine you should be able to adjust them in main.py. Just tweak the amount of time in the time.sleep calls. If your keybindings are different then you may want to reset them to default for this bot to work.