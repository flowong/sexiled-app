# home page for sexile app

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "hi michelle"

class Room:
	def __init__(self, status, location):
		self.s = status
		self.l = location



if __name__ == "__main__":
	app.run()