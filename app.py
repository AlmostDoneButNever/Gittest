app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello I am Angel!'

if __name__ == "__main__":
	app.run()
