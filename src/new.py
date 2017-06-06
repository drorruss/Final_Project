import sqlite3
import csv
import Adafruit_DHT as dht
import datetime
import time as ti
import os
import signal
from twilio.rest import TwilioRestClient

def check_exe(h,t):
   if (t >35 and t < 36.6) or (t < 38 and t > 37.2):
     print "Temprature Exeption - Please go to the baby !!"    
   if (t < 35 or t > 38):
     print ("Temprature Exeption - Please go rapidly to the baby !! ")  
   if (h > 25 and h < 30) or (h > 50 and h < 55):
     print ("Humidity Exeption - Please go to the baby !!")  
   if (h < 25 or h > 55):
     print ("Humidity Exeption - Please go rapidly to the baby !!")

def main():
  # account_sid = "AC6c0dbc8ae5b4ca4624001b3b4ea75cda"
  # auth_token = "f585e28caf77a953e2fcdf57ab1f13c1"
  # client = TwilioRestClient(account_sid, auth_token)
  # message = client.messages.create(to="+972525706612", from_="+19163785052",
                                     #body="Hello there!")     
   file = open('data'+'.txt', 'w+')
   print "Truncating the file...!"
   file.truncate()
   conn = sqlite3.connect('example.db')
   cur = conn.cursor()
   cur.execute('''CREATE TABLE data
             (Temprature text,Humidity text,Date text, Time text)''')
   global var
   var = 0
   while var <= 5 :
       h,t = dht.read_retry(dht.DHT22, 4)
       file.write('Temprature={0:0.1f}*C, Humidity={1:0.1f}% '.format(t, h))
       now = datetime.datetime.now()    #2014-09-26  16:34:40
       print now
       d = now.strftime("%Y-%m-%d")
       time =  now.strftime("%H:%M:%S")
       file.write ('Date=' + d)
       file.write (' Time=' + time)
       file.write('\n')
       #file.write(' Date=' now.strftime("%Y-%m-%d"))
       purchases = [(t,h,d,time)]
       cur.executemany('INSERT INTO data VALUES (?,?,?,?)',purchases)
       conn.commit()
       check_exe(h,t)
       var +=1


   dd = cur.execute("SELECT * FROM data")
   with open('history.csv', 'w') as f:
       writer = csv.writer(f)
       writer.writerow(['Temprature','Humidity','Date','Time'])
       writer.writerows(dd)
       #f.write(['Date','Time'])
       #f.write('\n')
       #for line in conn.iterdump():
        #   f.write('%s\n' % line)
        
   conn.close()
   file.close()
   
   os.remove('/home/pi/Desktop/example.db')
   os.remove('/home/pi/Desktop/data.txt')
   
def stop():
  signal.signal(signal.SIGTERM,handler)
  raise TypeError ('stoppp')

def handler(sig,frame):
   print "dror"


