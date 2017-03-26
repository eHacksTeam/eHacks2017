from appJar import gui
import classifier_lib as nn
import twitter_bot as tb

app = gui()

def press(name):
	print(nn.display_indicators(100))

def analyze(name):
	url = app.getEntry("urlbox")
	if url.lstrip()[0] is "@":
		try:
			tweets = tb.get_tweets_from_user(url.lstrip()[1:])
		except:
			app.warningBox("Username Error", "Username not found!")
			return

		probs =[]
		for tweet in tweets:
			probs.append(nn.get_prob_of_pos(tweet.text))

		average = round(sum(probs, 0.0) / len(probs),3)


		writefile = open("./user_prob.log", 'a')
		writefile.write(url+","+str(average)+"\n")
		writefile.close()

		app.setLabel("problabel","Average user harrassment probility")
		app.setEntry("probbox",str(average))
	else:
		statusid = url.split("/")[len(url.split("/"))-1]
		tweet = tb.get_tweet_by_status(statusid)
		print(tweet.text)
		app.setLabel("problabel","Tweet harrasment probility")
		app.setEntry("probbox",str(nn.get_prob_of_pos(tweet.text)))

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
	app.addButtons(["Analyze"], [analyze], 1, 1, 2)

	app.addHorizontalSeparator(2,0,4)

	app.addLabel("problabel", "Probability", 3, 0, 2) 
	app.addEntry("probbox", 4, 0, 2) 

	app.addButtons(["display indicators"], [press], 5, 0, 2)

	app.go()

if __name__ == "__main__":
    main()
