from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello Elaine, Mun Yuen and Sho yin, Angel is here!'

if __name__ == "__main__":
	app.run()
