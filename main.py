import sqlite3
import Adafruit_DHT as dht
import datetime


def create_csv(file):
    conn = sqlite3.connect('example.db')
    conn.text_factory = str 
    cur = conn.cursor()
    si= 'data.txt'
    data = cur.execute("SELECT * FROM '%s'" % si)
    with open('history.csv', 'w') as new:
        writer = writer(new)
        writer.writerow(['Temprature','Humidity', 'Date','Time'])
        writer.writerows(data)
        
        
file = open('data'+'.txt', 'w+')
print "Truncating the file...!"
file.truncate()
var = 1
while var <= 5 :
    h,t = dht.read_retry(dht.DHT22, 4)
    file.write('Temprature={0:0.1f}*C, Humidity={1:0.1f}%'.format(t, h))
    now = datetime.datetime.now()    #2014-09-26  16:34:40
    print now
    d = now.strftime("%Y-%m-%d")
    time =  now.strftime("%H:%M:%S")
    file.write ('Date=' + d)
    file.write (' Time=' + time)
    file.write('\n')
    #file.write(' Date=' now.strftime("%Y-%m-%d"))
    var = var + 1
file.close()

create_csv(file)

