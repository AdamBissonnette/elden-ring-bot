import time
# from helpers.autopy_helpers import AutopyHelpers
from helpers.win32_helpers import Win32Helpers

class Bot():
    def __init__(self):
        self.elden_ring_window = Win32Helpers.get_window('ELDEN RING™')

        # self.rest_palace_ledge = [
        #     AutopyHelpers.get_bitmap('assets/rest_palace_ledge.png')
        # ]

    def run_to_point(self):
        if not self.check_window():
            return False
        Win32Helpers.pressAndHold("spacebar", "w")
        time.sleep(2.5)
        Win32Helpers.release("spacebar", "w")
        time.sleep(0.5)
        Win32Helpers.pressAndHold("spacebar", "a")
        time.sleep(0.5)
        Win32Helpers.release("spacebar", "a")
        time.sleep(0.5)
        Win32Helpers.pressAndHold("spacebar", "w")
        time.sleep(0.7)
        Win32Helpers.release("spacebar", "w")
        time.sleep(0.5)
        return True

    def run_up_further(self):
        if not self.check_window():
            return False
        Win32Helpers.pressAndHold("spacebar", "w")
        time.sleep(6)
        Win32Helpers.release("spacebar", "w")
        time.sleep(0.5)
        return True

    def use_ability(self):
        if not self.check_window():
            return False
        Win32Helpers.press("ctrl")
        time.sleep(0.5)
        return True

    def teleport_back(self):
        if not self.check_window():
            return False
        Win32Helpers.press("g")
        time.sleep(0.5)
        Win32Helpers.press("f")
        time.sleep(0.5)
        Win32Helpers.press("e")
        time.sleep(0.5)
        Win32Helpers.press("e")
        time.sleep(6)
        return True

    def start_session(self):
        Win32Helpers.click_mouse(1000, 500)

    def do_routine(self):
        if not self.teleport_back(): return False
        if not self.run_to_point(): return False
        if not self.use_ability(): return False
        # Doesn't seem to be worth it
        # if not self.run_up_further(): return False
        # if not self.use_ability(): return False
        return True

    def check_window(self):
        activeWindow = Win32Helpers.get_active_window()
        return activeWindow == self.elden_ring_window

    def main(self):
        i = 0
        print("Starting session by clicking in the window")
        # startingWindow = Win32Helpers.get_active_window()
        self.start_session()
        while self.check_window():
            i += 1
            print("Starting iteration " + str(i))
            if not self.do_routine(): break
            time.sleep(8)
        print("Stopped session because we're no longer in the right window")
        return

if __name__ == '__main__':
    bot = Bot()
    bot.main()