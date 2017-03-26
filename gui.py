from appJar import gui
import classifier_lib as nn


def press(name):
	url = app.getEntry("urlbox")
	if url.lstrip()[0] is "@":
		print("runscript for username")
		app.setLabel("problabel","Average user harrassment probility")
	else:
		print("run script to get tweet")
		app.setLabel("problabel","Tweet harrasment probility")


def prob(name):
	tweet = app.getEntry("urlbox")
	print(tweet)
	probability = nn.get_prob_of_pos(tweet)
	print(probability)
	app.setEntry("probbox",probability)


app = gui()
app.addLabel("title","Mean Tweet Analyzer",0,0,2) 

app.addEntry("urlbox", 1, 0)
app.setEntry("urlbox","string input")
app.addButtons(["Analyze"], [press], 1, 1, 2)

app.addHorizontalSeparator(2,0,4)

app.addLabel("problabel", "Probability", 3, 0, 2) 
app.addEntry("probbox", 4, 0, 2) 

#app.addButtons(["display indicators"], [press], 4, 0, 2)

app.go()
