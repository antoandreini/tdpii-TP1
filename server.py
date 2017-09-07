from flask import Flask, render_template, request
from db_conf import connection
import json,pymysql.cursors

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/api/clima')
def clima():
	cnx = pymysql.connect(**connection)
	try:
		cursor = cnx.cursor()
		cursor.execute("SELECT temperatura,humedad,presion,viento FROM Clima ORDER BY id DESC LIMIT 0,1")
		t,h,p,v = cursor.fetchone()
		print "Clima segun bd: ",t," ",h," ",p," ",v
		cursor.execute("SELECT AVG(temperatura),AVG(humedad),AVG(presion),AVG(viento) FROM Clima ORDER BY id DESC LIMIT 0,10")
		avgt,avgh,avgp,avgv = cursor.fetchone()
                print "Promedios segun bd:",avgt," ",avgh," ",avgp," ",avgv
                return json.dumps({"temperatura":t,"avgtemperatura":avgt,"humedad":h,"avghumedad":avgh,"presion":p,"avgpresion":avgp,"viento":v,"avgviento":avgv})
	finally:
		cnx.close()

@app.route('/api/frecuencia',methods=['POST'])
def frecuencia():
	cnx = pymysql.connect(**connection)
	frec = request.form.get('frecuencia')
	try:
		cursor = cnx.cursor()
		cursor.execute("UPDATE Configuracion SET valor = "+frec+" WHERE clave = 'frecuencia'")
		cnx.commit()
	finally:
		cnx.close()
		return 'true'

if __name__ == '__main__':
    socketio.run(app)
