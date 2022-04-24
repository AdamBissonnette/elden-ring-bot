import time, autopy

class AutopyHelpers():
    def get_bitmap(file, debug=False):
        return {"name": file, "data": autopy.bitmap.Bitmap.open(file), "debug": debug}

    def find_bitmap(screen, bitmap, tolerance):
        found = screen.find_bitmap(bitmap["data"], tolerance)
        if bitmap["debug"]:
            AutopyHelpers.print_log("{} found {}".format(bitmap["name"], found))
        
        return found

    def tap_key():
        autopy.key.tap(autopy.key.Code.DELETE, [], 0.5)

    def find_asset(screen=None, assets=None, tolerance=0):
        if assets is None:
            return None

        if screen is None:
            screen = AutopyHelpers.refresh_screen()

        if isinstance(assets, list):
            for asset in assets:
                found_asset = AutopyHelpers.find_bitmap(screen, asset, tolerance)
                if found_asset:
                    return found_asset
        else:
            found_asset = AutopyHelpers.find_bitmap(screen, assets, tolerance)
            if found_asset:
                return found_asset

        return None

    def find_and_click_asset(assets, click_x_times=1, xoffset=0, yoffset=0,
                            tolerance=0, persistent=False, sleep_after_click=0.2,
                            screen=None, toggle_state=0):
        clicked = False
        click_attempted = False
        while not clicked:
            if screen is None:
                screen = AutopyHelpers.refresh_screen()
            asset = AutopyHelpers.find_asset(screen, assets, tolerance)
            if asset:
                AutopyHelpers.click_asset(asset, click_x_times, xoffset, yoffset, sleep_after_click, toggle_state)
                time.sleep(0.1)
                click_attempted = True
            else:
                if click_attempted:
                    clicked = True
                else:
                    clicked = False
                    break
            screen = None
            if not persistent:
                clicked = True
            else:
                time.sleep(0.5)

        return clicked

    def click_asset(found_asset, count=1, xoffset=0, yoffset=0,
                     sleep_after_click=0.1, toggle_state=0):
        autopy.mouse.move(found_asset[0]+xoffset, found_asset[1]+yoffset)
        # coords = win32api.MAKELONG(int(found_asset[0]+xoffset), int(found_asset[1]+yoffset))

        for _ in range(0,count):
            # AutopyHelpers.post_button_click(coords)
            if toggle_state == 0:
                autopy.mouse.click()
            elif toggle_state == 1:
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
            elif toggle_state == 2:
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)
            time.sleep(sleep_after_click)

    def refresh_screen(size=1):
        slow_mode = False
        screen = None
        x = 0
        y = 0

        # screen = None
        crop = ((x,y), (390,727))

        if size == 1:
            crop = ((x,y), (390,727))
        elif size == 2:
            crop = ((x,y), (390,350))
            # screen = autopy.bitmap.capture_screen(((0,0), (390,350)))
        elif size == 3:
            crop = ((x,y+125), (390,225))
        else:
            crop = ((x+197,y+30), (40,30))

        if screen and slow_mode:
            screen = screen.cropped(crop)
        else:
            screen = autopy.bitmap.capture_screen(crop)

        return screen