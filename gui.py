from appJar import gui
import classifier_lib as nn


def press(name):
	#print("run script to get tweet")
	print(nn.display_indicators(100))


def prob(name):
	tweet = app.getEntry("urlbox")
	print(tweet)
	probability = nn.get_prob_of_pos(tweet)
	print(probability)
	app.setEntry("probbox",probability)


app = gui()
app.addLabel("title","Mean Tweet Analyzer",0,0,2) 

app.addEntry("urlbox", 1, 0, 2)
app.setEntry("urlbox","string input")
app.addButtons(["Analyze"], [prob], 1, 1, 2)

app.addHorizontalSeparator(2,0,4)

app.addEntry("probbox", 3, 0) 
app.addLabel("problabel", "Probability of harrasment:", 3, 1) 

app.addButtons(["display indicators"], [press], 4, 0, 2)

app.go()
