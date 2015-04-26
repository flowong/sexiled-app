from flask import Flask, render_template
from flask import request
from flask.ext.pymongo import PyMongo

app = Flask("carlsex")
mongo = PyMongo(app)

@app.route('/')
def home():
	db = mongo.db
	# for thing in mongo.db.roomdata.find():
	# 	print thing
	FLOOR_NUM = 1
	ROOM_NUM = '107A'
	DORM = 'Allen House'
	dorm = db.roomdata.find({'name': DORM})[0]
	for floor in dorm['floors']:
		if floor['number'] == FLOOR_NUM:
			print floor
			for room in floor['rooms']:
				if room['name'] == ROOM_NUM:
					room['size'] = '2'
	db.roomdata.update({'name': 'Allen House'}, dorm)
	return render_template('home.html')

@app.route('/havingsex')
def havingsex():
	return render_template('havingsex.html')

@app.route('/bedlook')
def bedlook():
	return render_template('bedlook.html')

@app.route('/confirmation')
def confirmation():
	print "aah"
	error = None
	if request.method == "POST":
		print "helo"
		if valid_havingsex(request.form['name']):
			print "name thing", valid_havingsex(request.form['name'])
			return 
		else:
			error = "error"
	return render_template('confirmation.html', error=error)
if __name__ == "__main__":
	# print dir(mongo)
	# print mongo.db
	# conn = mongo.MongoClient()
	# print mongo.carlsex.roomdata.find()
	app.run(debug=True)