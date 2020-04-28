import os
import time
import RPi.GPIO as GPIO

FAN_ON_MODE = 42  # (In celsius) The upper temperature threshold at which cooling is turned on.
FAN_OFF_MODE = 40  # (In celsius) Lower temperature threshold at which cooling is turned off
SLEEP_INTERVAL = 2  # (In seconds) Temperature Check Interval
SLEEP_INTERVAL_FAN = 5  # (In seconds) Temperature Check Interval
FAN_PIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)    
#https://www.element14.com/community/servlet/JiveServlet/downloadImage/102-92640-8-726998/GPIO-Pi4.png

def measure_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C","").replace("\n",""))

    temp=int(float(getCPUtemperature()))
    return float(temp)



while True:
        #print(measure_temp())
        temp = measure_temp()
        temp = float(temp) * 1
        
        if(temp > FAN_ON_MODE):
                 print('FAN ON')
                 print(temp)
                 GPIO.output(FAN_PIN, True)
                 time.sleep(SLEEP_INTERVAL_FAN)
        elif (temp > FAN_OFF_MODE):
                 print('FAN OFF')
                 print(temp)
                 GPIO.output(FAN_PIN, False)
                 time.sleep(SLEEP_INTERVAL)
                 continue
        time.sleep(SLEEP_INTERVAL)   
GPIO.cleanup()    
