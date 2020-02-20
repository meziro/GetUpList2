# cording UTF-8
import datetime
import time
import pygame.mixer
import RPi.GPIO as GPIO
import subprocess
import os
#set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.IN)
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

def getdis():
	GPIO.output(17,GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(17,GPIO.LOW)
	pingtime = pulseIn(18,GPIO.HIGH,13200)
	distance = pingtime*340/2/10000
	return distance

def pulseIn(pin,level,timeout):
	t=time.time()
	while(GPIO.input(pin) != level):
		if((time.time()-t)> timeout*0.000001):
			return 0
	t=time.time()
	while(GPIO.input(pin) == level):
		if((time.time()-t)> timeout*0.000001):
			return 0
	pulsetime = (time.time()-t)*1000000
	return pulsetime
	
	

get_hour = input()
get_min = input()
musicon = 0
print(pygame.mixer.music.get_busy())
while(1):
	GetTime = (get_hour*100)+get_min
	Nowclock = datetime.datetime.now()
	NowTime = (Nowclock.hour*100)+Nowclock.minute
	print(GetTime)
	print(NowTime)
	print(pygame.mixer.music.get_volume())
	print(getdis())
        if(GetTime == NowTime):
		while(pygame.mixer.music.get_busy()==0):
			pygame.mixer.music.load("/home/pi/Downloads/bgm_maoudamashii_neorock83.mp3")
			pygame.mixer.music.play(-1)
                if(getdis()<15.0):
		    pygame.mixer.music.set_volume(0.5)
		    f = open('GetUpList.txt','a')
		    f.write('%d %d %d %d %d\n' % (Nowclock.year,Nowclock.month,Nowclock.day,Nowclock.hour,Nowclock.minute))
		    f.close()

		    comment = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
		    os.system('git add .')
		    os.system('git commit -m {}'.format(comment))
		    os.system('git push')

	if((GetTime == NowTime-1 and pygame.mixer.music.get_volume() <= 0.5) or (GetTime == NowTime-2 and pygame.mixer.music.get_volume() <=0.6)or( GetTime == NowTime-3 and pygame.mixer.music.get_volume() <=0.7)or (GetTime == NowTime-4 and pygame.mixer.music.get_volume() <=0.8)or (GetTime == NowTime-5 and pygame.mixer.music.get_volume() <=0.9)):
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.1)
	time.sleep(3)
