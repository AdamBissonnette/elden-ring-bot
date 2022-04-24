# elden-ring-bot
A bot to farm palace ledge with late game junk

## Installation

* pip install virtualenv
* Install python 382 https://www.python.org/downloads/release/python-382/
* py -3.8-32 -m virtualenv py3832
* .\py3832\Scripts\activate
* python -m pip install requirements.txt

## Run Requirements

* Must be at the Palace Approach site of grace
* Must have the Sacred Relic sword and sufficient stats to clear mobs

## Running

* Go to the Palace Approach Ledge-Road with fancy sword equipped
* Run `python main.py`

## TODO

* Determine if running forward and killing more mobs is worth it
* Cleanup autopy stuff or use it for reading images etc...

## How to click and tap keys in elden ring with Win32
* win32api.SetCursorPos((1000,1000))                            
* win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 1000, 1000, 0, 0)
* win32api.keybd_event(17, win32api.MapVirtualKey(17,0), 0, 0)
* time.sleep(0.5)
* win32api.keybd_event(17, win32api.MapVirtualKey(17,0), win32con.KEYEVENTF_KEYUP, 0)