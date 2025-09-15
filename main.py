import sys,traceback,os
import time
from ahk import AHK
import re
ahk = AHK(version="v2")

class Window():
    def __init__(self):
        super().__init__()
        self.running = False
        self.startTime = input("Enter the delay: ")
        self.StartAFK()
    def SendInput(self,window,active_window):
        try:
            def Release():
                try:
                    ahk.key_up("space")
                except Exception as e:
                    print(e)
            if not self.running: 
                return
            window.activate()
            ahk.key_down("space")
            time.sleep(0.5)
            Release()
        except Exception as e:
            print("AHK error:", e)
    def OpenRobloxWindow(self):
        
        try:
            if self.firstStart == True:
                self.firstStart = False
            active_window = ahk.active_window
            for window in ahk.windows():
                if window.get_class() == "WINDOWSCLIENT" or window.get_class() == "ApplicationFrameWindow":
                    title = window.get_title()
                    title_norm = " ".join(title.replace("\u00A0", " ").split()).lower()
                    if (re.search(r"\broblox\b", title_norm)
                    and not re.search(r"\broblox studio\b", title_norm)
                    and not re.search(r"\banti afk frozen\b", title_norm)):
                        time.sleep(0.200)
                        self.SendInput(window,active_window)
            time.sleep(0.200)
            active_window.activate()
            time.sleep(self.delayTime)
            self.OpenRobloxWindow()
        except Exception as e:
            tb = traceback.format_exc() 

    def on_error(self, tb: str):
            print("Error captured:", tb)

    def StartAFK(self):
        try:
            self.firstCall = True
            text = self.startTime
            if self.running == False:
                if text.isdigit():
                    text = int(text)
                    if text <= 60*19 and text >= 5:
                        print("Loading")
                        self.running = True
                        self.firstStart = True
                        self.delayTime = text
                        print("AFK Enabled")
                        time.sleep(0.1)
                        self.OpenRobloxWindow()
        except Exception as e:
            print("Start Error: ",e)



window = Window()
sys.exit()