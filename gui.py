from appJar import gui
import classifier_lib as nn
import twitter_bot as tb

#tweetnumber = 10
app = gui()
#app2 = gui()

# def updatelabel(name):
# 	tweetnumber = int(app2.getEntry("numbox"))
# 	print("this is where my for loop would go, IF I HAD ONE", tweetnumber)
# 	app2.stop()

# def stop(name):
# 	app2.stop()


def press(name):
	url = app.getEntry("urlbox")
	if url.lstrip()[0] is "@":
		user = tb.get_user(url.lstrip()[1:])
		print(user.id)
		tweets = tb.get_tweets_from_user(user.name)
		print(tweets[0].text)
		print("runscript for username")

		# app2.go()
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


def main():

	app.addLabel("title","Mean Tweet Analyzer",0,0,2) 

	app.addEntry("urlbox", 1, 0)
	app.setEntry("urlbox","URL or @username")
	app.addButtons(["Analyze"], [press], 1, 1, 2)

	app.addHorizontalSeparator(2,0,4)

	app.addLabel("problabel", "Probability", 3, 0, 2) 
	app.addEntry("probbox", 4, 0, 2) 



	# app2.addLabel("title","How many tweets do you want to assess",0,0,2) 
	# app2.addNumericEntry("numbox",10)
	# app2.addButtons(["Ok", "Cancel"], [updatelabel, stop])

	#app.addButtons(["display indicators"], [press], 4, 0, 2)

	app.go()

if __name__ == "__main__":
    main()
