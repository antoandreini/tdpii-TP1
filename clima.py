import pymysql.cursors,time,random
from db_conf import connection

cnx = pymysql.connect(**connection)

def temp():
	return random.uniform(14, 20)

def hum():
	return random.uniform(80,95)

def pres():
	return random.uniform(1000,1050)

def viento():
	return random.uniform(15,18)

def clima():
	return (temp(),hum(),pres(),viento())

while(1):
	cursor = cnx.cursor()
	cursor.execute("SELECT valor FROM Configuracion where clave = 'frecuencia'")
	frec = cursor.fetchone()[0]
	print "Frecuencia es: ", frec
	cursor = cnx.cursor()
	tmp = clima()
	cursor.execute("INSERT INTO Clima (temperatura,humedad,presion,viento) VALUES (%s,%s,%s,%s)",tmp)
	cnx.commit()
	print "Los valores insertados son: ", tmp
	time.sleep(float(frec))

