from flask import Flask, render_template, redirect, request, url_for
from keras.models import load_model
import numpy as np
from PIL import Image 



# ________________________ RELOAD PRE-TRAINED MODEL ________________________

MODEL = load_model('model.h5')


# _______________________________ APP ROUTES _______________________________

app = Flask(__name__)


@app.route("/")
def index():

	return render_template("index.html")



@app.route("/upload", methods=["POST", "GET"])
def upload():

	return render_template("upload.html")



@app.route("/result", methods=["POST", "GET"])
def result():

	if request.method == "POST":
		file = request.files["picture"]


	features = []

	a = Image.open(file).convert("1")
	a = a.resize((28, 28))
	b = list(a.getdata())
	features.append(b)

	x = np.array(features)

	x2 = x.reshape(-1, 28, 28, 1)

	x2 = x2 / 255

	result = MODEL.predict(x2)

	predected = None

	string = None

	for item in result.round():
		for index, value in enumerate(item):
			if value == 1:
				predected = index
	if predected == 0:
		string = "Zero"
	elif predected == 1:
		string = "One"
	elif predected == 2:
		string = "Two"
	elif predected == 3:
		string = "Three"
	elif predected == 4:
		string = "Four"
	elif predected == 5:
		string = "Five"
	elif predected == 6:
		string = "Six"
	elif predected == 7:
		string = "Seven"
	elif predected == 8:
		string = "Eight"
	elif predected == 9:
		string = "Nine"
	else:
		string = "Sorry"
		

	return render_template("result.html", number=predected, string=string)




