from m5stack import *
from m5ui import *
from uiflow import *
import time

def color_pause(color,duration):
    lcd.rect(20, 90, 100, 40, color=0xFFFFFF)
    lcd.text(25, 95, "Shawty", color=0xFF0000)
    setScreenColor(color)
    time.sleep_ms(duration)

def flash_text(duration, stop):
    count = 0
    while count < stop:
        
        count += 1
        color_pause(0xf0f00, duration)

flash_rgb(500, 20)