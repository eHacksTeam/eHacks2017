from appJar import gui
import neural as nn
import string

def press(name):
	#print("run script to get tweet")
	print(nn.display_indicators(100))

def prob(name):
	tweet = app.getEntry("urlbox")
	print(tweet)
	probility = nn.get_prob_of_pos(tweet)
	print(probility)
	app.setEntry("probbox",probility)


app = gui()
app.addLabel("title","Mean Tweet Analyzer",0,0,2) 

app.addEntry("urlbox", 1, 0, 2)
app.setEntry("urlbox","string input")
app.addButtons(["Analyze"], [prob], 1, 1, 2)

app.addHorizontalSeparator(2,0,4)

app.addEntry("probbox", 3, 0) 
app.addLabel("problabel", "Probibility of harrasment:", 3, 1) 

app.addButtons(["display indicators"], [press], 4, 0, 2)

app.go()