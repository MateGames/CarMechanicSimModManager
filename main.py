import pygame
import os
from time import sleep, time
from keyboard import wait, is_pressed
from pyautogui import press, write
import win32gui
import win32con
import win32api

# variables
width = 600 
height = 400










def setup():
    screen_width = 2560
    x = screen_width - width
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










class KillApp():
    def __init__(self) -> None:
        self.start = 0
        self.kill = False
        
    def update(self):
        if is_pressed("t") and not self.kill:
            self.start = time()
            self.kill = True
        
        if not is_pressed("t"):
            self.kill = False  


        if time() - self.start > 3 and self.kill:
            return False
        
        return True






screen = setup()
killApp = KillApp()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # update
    run = killApp.update()    
    
    

    # display
    screen.fill((0, 0, 0))
    
    
    pygame.draw.rect(screen,(200,0,0),(0,0,width,height),2) # temp boundary



    pygame.display.update()
pygame.quit()
