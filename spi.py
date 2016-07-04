#! python
# -*- coding: UTF-8 -*-
import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
a=u"°C"

while True:

	resp = spi.xfer([0x00,0x00])
    	time.sleep(0.5)
	temp = (((resp[0]*256/8)*0.25)+((resp[1]/8)*0.25))-2.25
	print "Temperatur : %d%s" %(temp,a)
        
	time.sleep(0.5)
