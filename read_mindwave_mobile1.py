import time
import RPi.GPIO as gpio
import bluetooth
from MindwaveDataPoints import RawDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader
from MindwaveDataPoints import AttentionDataPoint
from MindwaveDataPoints import DataPoint

gpio.setmode(gpio.BOARD)
Motor1A = 35
Motor1B = 36
Motor2A = 38
Motor2B = 40
gpio.setup(Motor1A, gpio.OUT)
gpio.setup(Motor1B, gpio.OUT)
gpio.setup(Motor2A, gpio.OUT)
gpio.setup(Motor2B, gpio.OUT)

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    
    while(True):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        if (dataPoint.__class__.__name__=='AttentionDataPoint'):
		if (int(dataPoint) > 60):
			print (dataPoint)
			print "Threshold reached! You are moving."
			gpio.output(Motor1A,gpio.HIGH)
			gpio.output(Motor1B,gpio.LOW)
			gpio.output(Motor2A,gpio.HIGH)
			gpio.output(Motor2B,gpio.LOW)
			time.sleep(2)
			#break
		else:
			print(dataPoint)
			print "Sorry!You are not concentrating."
			gpio.output(Motor1A,gpio.LOW)
			gpio.output(Motor1B,gpio.LOW)
			gpio.output(Motor2A,gpio.LOW)
			gpio.output(Motor2B,gpio.LOW)
			time.sleep(1)

