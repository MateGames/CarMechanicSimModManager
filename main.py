import pygame
import os
from time import time #sleep: DONT USE SLEEP, FREEZ RUNING PROGRAM!!!!!!!!! 
from keyboard import wait, is_pressed
from pyautogui import press, write
import win32gui
import win32con
import win32api


# variables
width = 300
height = 200










def setup():
    screen_width = 2560
    x = 0
    y = 0

    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

    pygame.init()
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    pygame.display.set_caption("Transparent Overlay")

    hwnd = pygame.display.get_wm_info()["window"]

    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, width, height, 0)

    win32api.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32api.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 0, win32con.LWA_COLORKEY)

    return screen










class KillApp:
    def __init__(self,button) -> None:
        self.start = 0
        self.kill = False
        self.timeout = 2
        self.button = button
        
        
    def update(self) -> bool:
        if is_pressed(self.button) and not self.kill:
            self.start = time()
            self.kill = True
        
        if not is_pressed(self.button):
            self.kill = False  

        if time() - self.start > self.timeout and self.kill:
            return False
        
        return True
    
    
    def display(self) -> None:
        if self.kill:
            pygame.draw.line(screen, (222,0,0), (0,0), (0,(time() - self.start) / self.timeout * height),10)










class Helo():
    def update():
        ...
        
    def display():
        ...










class AutoBuy():
    def update():
        ...
        
    def display():
        ...










class App:
    def __init__(self, screen) -> None:
        self.scene = Helo()
        self.screen = screen
        self.FPS = 60
        self.mods = [Helo(),AutoBuy()]
        

    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        killApp = KillApp('t')
        
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            # update
            run = killApp.update()    
            
            

            # display
            self.screen.fill((0, 0, 0))
            killApp.display()
            
            pygame.draw.rect(self.screen,(200,200,10),(0,0,width,height),2) # temp boundary



            pygame.display.update()
            clock.tick(self.FPS)
        pygame.quit()



if __name__ == "__main__":
    screen = setup()
    app = App(screen)
    app.run()