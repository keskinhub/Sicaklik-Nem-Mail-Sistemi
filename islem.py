import RPi.GPIO as GPIO
import dht11
import time
import datetime
import smtplib
 

mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo() 
mail.starttls()
mail.login("mailAdresin","mailSifren")


# GPIO başlatma
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# raspberry üzerinden verilerin sensörle transferinin yapıldığı pin(14)
instance = dht11.DHT11(pin=14)

while True:
    result = instance.read()
    if result.is_valid():
        mail.sendmail("GondericiMailAdresi","AliciMailAdresi","Subject: Gunluk Hava Durumu \nMerhaba ,\n\r Bugun Hava Sicakligi= "+repr(result.temperature) +"C derece, Nem = " + repr(result.humidity))        
    
    time.sleep(5)
