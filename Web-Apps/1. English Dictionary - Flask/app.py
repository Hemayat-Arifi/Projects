from flask import Flask, render_template, request, url_for
from wordnik import *
import requests
from urllib.request import urlopen, HTTPError
from datetime import datetime


app = Flask(__name__)


# ___________________________________ API Setup ______________________________________

apiUrl = 'http://api.wordnik.com/v4'
apiKey = '6hljwiih61chg15p9a4ih0q0jm574ygovxp8ealdzp2v1jm2g'
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordApi.WordApi(client)

catagories = ['getAudio', 'getDefinitions', 'getEtymologies', 'getExamples', 'getHyphenation', 'getPhrases', 'getRelatedWords', 'getScrabbleScore', 'getTextPronunciations', 'getTopExample', 'getWord', 'getWordFrequency']

getDefinitions_catagories = ['attributionText', 'attributionUrl', 'citations', 'exampleUses', 'extendedText', 'labels', 'notes', 'partOfSpeech', 'relatedWords', 'score', 'seqString', 'sequence', 'sourceDictionary', 'swaggerTypes', 'text', 'textProns', 'word']


# ___________________________________ App Routes _____________________________________

@app.route("/")
def main():

	return render_template("index.html")



@app.route("/result", methods=["POST", "GET"])
def result():

	try:	
		word = request.form["word"]

		word_definition = wordApi.getDefinitions(word)

		word_example = wordApi.getExamples(word)

		word_sound = wordApi.getAudio(word)

		definition = [word_definition[i].text for i in range(len(word_definition))]

		definition_final = []

		if len(definition) == 1:
			definition_final.append(definition[0])
		elif len(definition) > 1:
			definition_final.append(definition[0])
			definition_final.append(definition[1])
		else:
			definition_final.append("None")

		examples = [word_example.examples[i].text for i in range(len(word_example.examples))]

		sound = []

		if len(word_sound) == 1:

			sound_female = word_sound[0].fileUrl
			sound.append(sound_female)
		elif len(word_sound) == 2:
			sound_male = word_sound[1].fileUrl
			sound_female = word_sound[0].fileUrl
			sound.append(sound_female)
			sound.append(sound_male)
		else:
			sound.append("None")


	except HTTPError:
		return "<h1>Wrong Text or word form you might entered the plural or past form of the word type the genuine word</h1>"
	else:
		pass
	finally:
		pass
	

	return render_template("result.html", word=word, definition=definition, examples=examples, definition_final=definition_final, sound=sound)



@app.route("/word-of-the-day")
def word_of_the_day():

	date = datetime.now()
	month = date.month
	day = date.day

	try:	
		new = requests.get("https://api.wordnik.com/v4/words.json/wordOfTheDay?date=2022%2F{}%2F{}&api_key=6hljwiih61chg15p9a4ih0q0jm574ygovxp8ealdzp2v1jm2g".format(month, day))

		a = new.json()
		word = a["word"]		

		word_definition = a["definitions"][0]["text"]

		word_example = a["examples"][0]["text"]

	except HTTPError:
		return "<h1>Wrong Text or word form you might entered the plural or past form of the word type the genuine word</h1>"
	else:
		pass
	finally:
		pass
	

	return render_template("word_day.html", word=word, definition=word_definition, example=word_example)





