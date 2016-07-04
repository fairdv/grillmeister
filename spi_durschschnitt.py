import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
import spidev
import time
import datetime
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty

class Controller(App):
   
    info = StringProperty()
    spi = spidev.SpiDev()  
    spi.open(0,0)
    i = 0
    temp = 0
    global tempq 
    tempq = 0
    while i<10:	
	    resp = spi.xfer([0x00,0x00])
	    time.sleep(0.3)
	    temp = (((resp[0]*256/8)*0.25)+((resp[1]/8)*0.25))-2.25
	    tempq = tempq + temp
	    temp = 0
	    i= i+1
	    tempq = tempq/10         

    
    def do_sollwert(self):
		pass
if __name__ == '__main__':
    Controller().run()
