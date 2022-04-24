import time
import win32con
import win32api
import win32ui
import win32gui
import ctypes

class Win32Helpers():
    VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}

    def make_coords(x, y):
        return win32api.MAKELONG(x, y)

    def get_active_window():
        return win32gui.GetForegroundWindow()

    def get_window(name):
        window = win32gui.FindWindow(None, name)
        return window
    
    def click_mouse(x, y):
        win32api.SetCursorPos((x,y))
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def handle_keyboard_event(key, modifier, event, event_modifier):
        win32api.keybd_event(key, win32api.MapVirtualKey(key,0), event, event_modifier)

    def set_window(window):
        win32gui.SetActiveWindow(window)

    def post_button_click(window, coords=1000, stime=0.1, key=1):
        win32gui.SendMessage(window, win32con.WM_MOUSEMOVE, 0, coords)
        if key == 1:
            win32gui.SendMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, coords)
            win32gui.SendMessage(window, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, coords)
        else:
            win32gui.SendMessage(window, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, coords)
            win32gui.SendMessage(window, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, coords)
        time.sleep(stime)
        Win32Helpers.move_mouse(window, coords)


    def press(*args):
        '''
        one press, one release.
        accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
        '''
        for i in args:
            Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[i], 0,0,0)
            time.sleep(.05)
            Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)

    def pressAndHold(*args):
        '''
        press and hold. Do NOT release.
        accepts as many arguments as you want.
        e.g. pressAndHold('left_arrow', 'a','b').
        '''
        for i in args:
            Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[i], 0,0,0)
            time.sleep(.05)
            
    def pressHoldRelease(*args):
        '''
        press and hold passed in strings. Once held, release
        accepts as many arguments as you want.
        e.g. pressAndHold('left_arrow', 'a','b').

        this is useful for issuing shortcut command or shift commands.
        e.g. pressHoldRelease('ctrl', 'alt', 'del'), pressHoldRelease('shift','a')
        '''
        for i in args:
            Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[i], 0,0,0)
            time.sleep(.05)
                
        for i in args:
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
                time.sleep(.1)
                
            

    def release(*args):
        '''
        release depressed keys
        accepts as many arguments as you want.
        e.g. release('left_arrow', 'a','b').
        '''
        for i in args:
            Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)


    def typer(string=None,*args):
    ##    time.sleep(4)
        for i in string:
            if i == ' ':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['spacebar'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['spacebar'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '!':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['1'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['1'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '@':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['2'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['2'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '{':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['['], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['['],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '?':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['/'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['/'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == ':':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[';'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[';'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '"':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['\''], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['\''],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '}':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[']'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[']'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '#':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['3'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['3'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '$':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['4'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['4'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '%':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['5'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['5'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '^':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['6'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['6'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '&':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['7'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['7'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '*':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['8'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['8'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '(':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['9'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['9'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == ')':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['0'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['0'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '_':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['-'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['-'],0 ,win32con.KEYEVENTF_KEYUP ,0)


            elif i == '=':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['+'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['+'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '~':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['`'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['`'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '<':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[','], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[','],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == '>':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['.'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['.'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'A':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['a'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['a'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'B':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['b'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['b'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'C':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['c'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['c'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'D':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['d'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['d'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'E':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['e'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['e'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'F':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['f'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['f'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'G':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['g'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['g'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'H':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['h'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['h'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'I':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['i'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['i'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'J':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['j'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['j'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'K':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['k'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['k'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'L':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['l'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['l'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'M':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['m'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['m'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'N':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['n'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['n'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'O':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['o'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['o'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'P':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['p'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['p'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'Q':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['q'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['q'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'R':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['r'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['r'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'S':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['s'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['s'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'T':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['t'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['t'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'U':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['u'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['u'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'V':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['v'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['v'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'W':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['w'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['w'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'X':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['x'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['x'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'Y':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['y'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['y'],0 ,win32con.KEYEVENTF_KEYUP ,0)

            elif i == 'Z':
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'], 0,0,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['z'], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE['z'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        
            else:    
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[i], 0,0,0)
                time.sleep(.05)
                Win32Helpers.handle_keyboard_event(Win32Helpers.VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)

    def move_mouse(window, coords):
        win32gui.SendMessage(window, win32con.WM_MOUSEMOVE, 0, coords)

    def get_window_position(window, maxheight=-1):
        left, top, right, bot = win32gui.GetClientRect(window)
        return left, top