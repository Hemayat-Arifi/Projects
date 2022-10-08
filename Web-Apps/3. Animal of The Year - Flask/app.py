from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def language():
	return render_template("language.html")


@app.route("/english", methods=["POST", "GET"])
def eng():
	return render_template("english.html")


@app.route("/persian", methods=["POST", "GET"])
def persian():
	return render_template("persian.html")


@app.route("/english/result", methods=["POST", "GET"])
def resulteng():
	name = request.form["name"]
	year = request.form["year"]
	month = request.form["month"]
	age = int(year)
	animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit",
				"Dragon", "Snake", "Horse", "Sheep"]
	
	animal = int(year) / 12 % 1
	animal_of_the_year = None
	if animal == 0:
		animal_of_the_year = animals[0]
	else:
		animal_of_the_year = animal * 12
		final = round(animal_of_the_year)

	final_animal = animals[final]

	personality = {
		"Rat": "quick-witted, resourceful, versatile, kind.",
		"Ox": "diligent, dependable, strong, determined.",
		"Tiger": "brave, confident, competitive, unpredictable.",
		"Rabbit": "quiet, elegant, kind, responsible.",
		"Dragon": "confident, intelligent, enthusiastic.",
		"Snake": "enigmatic, intelligent, wise.",
		"Horse": "animated, active, energetic.",
		"Goat": "calm, gentle, sympathetic.",
		"Monkey": "sharp, smart, curious.",
		"Rooster": "observant, hardworking, courageous.",
		"Dog": "lovely, honest, prudent.",
		"Pig": "compassionate, generous, diligent."
	}

	lucky_number = {
		"Rat": [2, 3],
		"Ox": [1, 4],
		"Tiger": [1, 3, 4],
		"Rabbit": [3, 4, 6],
		"Dragon": [1, 6, 7],
		"Snake": [2, 8, 9],
		"Horse": [2, 3, 7],
		"Goat": [2, 7],
		"Monkey": [4, 9],
		"Rooster": [5, 7, 8],
		"Dog": 	[3, 4, 9],
		"Pig": [2, 5, 8],
	}


	return render_template("resulteng.html", name=name, year=year, month=month, age=age, animal=final_animal, personality=personality, number=lucky_number)



@app.route("/persian/result", methods=["POST", "GET"])
def resultper():
	name = request.form["name"]
	year = request.form["year"]
	month = request.form["month"]
	age = int(year)
	animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit",
				"Dragon", "Snake", "Horse", "Goat"]
	
	animal = int(year) / 12 % 1
	animal_of_the_year = None
	final_animal = None

	if animal == 0:
		animal_of_the_year = animals[0]
		final_animal = animal_of_the_year
	else:
		animal_of_the_year = animal * 12
		final = round(animal_of_the_year)

		final_animal = animals[final]

	personality = {
		"Rat": "زودباور, مدبر, همه کاره, مهربان.",
		"Ox": "کوشا, قابل اعتماد, قوی, مشخص",
		"Tiger": "شجاع, مطمئن, رقابتی, غیر قابل پیش بینی",
		"Rabbit": "ساکت, ظریف, مهربان, مسئول",
		"Dragon": "مطمئن, باهوش, مشتاق",
		"Snake": "معمایی, باهوش, عاقل",
		"Horse": "متحرک, فعال, پر انرژی",
		"Goat": "آرام, ملایم, دلسوز",
		"Monkey": "تیز, هوشمندانه, کنجکاو.",
		"Rooster": "ناظر, سخت کوش, شجاع",
		"Dog": "دوست داشتني, صادقانه, محتاط، معقول",
		"Pig": "دلسوز, سخاوتمندانه, کوشا"
	}

	lucky_number = {
		"Rat": [2, 3],
		"Ox": [1, 4],
		"Tiger": [1, 3, 4],
		"Rabbit": [3, 4, 6],
		"Dragon": [1, 6, 7],
		"Snake": [2, 8, 9],
		"Horse": [2, 3, 7],
		"Goat": [2, 7],
		"Monkey": [4, 9],
		"Rooster": [5, 7, 8],
		"Dog": 	[3, 4, 9],
		"Pig": [2, 5, 8],
	}

	animal_in_persian = None

	if final_animal == "Monkey":
		animal_in_persian = "میمون"
	elif final_animal == "Rooster":
		animal_in_persian = "خروس"
	elif final_animal == "Dog":
		animal_in_persian = "سگ"
	elif final_animal == "Pig":
		animal_in_persian = "خوک"
	elif final_animal == "Rat":
		animal_in_persian = "موش"
	elif final_animal == "Ox":
		animal_in_persian = "گاو"
	elif final_animal == "Tiger":
		animal_in_persian = "ببر"
	elif final_animal == "Rabbit":
		animal_in_persian = "خرگوش"
	elif final_animal == "Dragon":
		animal_in_persian = "اژدها"
	elif final_animal == "Snake":
		animal_in_persian = "مار"
	elif final_animal == "Horse":
		animal_in_persian = "اسب"
	elif final_animal == "Goat":
		animal_in_persian = "بز"



	return render_template("resultper.html", name=name, year=year, month=month, age=age, animal=final_animal, personality=personality, number=lucky_number, animal_in_persian=animal_in_persian)


