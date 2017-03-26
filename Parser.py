import csv
import sqlite3

def create_csv(file):
    conn = sqlite3.connect('example.db')
    conn.text_factory = str 
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM txt"+str(file))
    with open('history'+str(file)+'.csv', 'w') as new:
        writer = csv.writer(new)
        writer.writerow(['Temprature','Humidity', 'Date','Time'])
        writer.writerows(data)
