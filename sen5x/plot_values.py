import psycopg2
import matplotlib.pyplot as plt

#establishing the connection
conn = psycopg2.connect(
   database="sensors", user='sensors', password='your_password', host='localhost', port= '5432'
)

conn.autocommit = True
cursor = conn.cursor()
cursor.execute('''SELECT temperature from sen55''')
temperature = cursor.fetchall()
cursor.execute('''SELECT humidity from sen55''')
humidity = cursor.fetchall()
cursor.execute('''SELECT pm1 from sen55''')
pm1 = cursor.fetchall()
cursor.execute('''SELECT pm2_5 from sen55''')
pm2_5 = cursor.fetchall()
cursor.execute('''SELECT pm4 from sen55''')
pm4 = cursor.fetchall()
cursor.execute('''SELECT pm10 from sen55''')
pm10 = cursor.fetchall()
cursor.execute('''SELECT voc from sen55''')
voc = cursor.fetchall()
cursor.execute('''SELECT nox from sen55''')
nox = cursor.fetchall()

temperature = [float(t[0]) for t in temperature]
humidity = [float(h[0]) for h in humidity]
pm1 = [float(p[0]) for p in pm1]
pm2_5 = [float(p[0]) for p in pm2_5]
pm4 = [float(p[0]) for p in pm4]
pm10 = [float(p[0]) for p in pm10]
voc = [float(v[0]) for v in voc]
nox = [float(n[0]) for n in nox]





plt.plot(temperature, label="Temperature")
plt.plot(humidity, label="Humidity")
plt.legend()
plt.show()

plt.plot(pm1, label="PM1")
plt.plot(pm2_5, label="PM2.5")
plt.plot(pm4, label="PM4")
plt.plot(pm10, label="PM10")
plt.legend()
plt.show()

plt.plot(voc, label="voc")
plt.legend()
plt.show()

plt.plot(nox, label="nox")
plt.legend()
plt.show()
