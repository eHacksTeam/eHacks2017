import pickle


test = [("YES! And NOT a great day for RUSSIAN STEEL! Whoever said that is a traitor and will be PUNISHED! By being sent to a GULAG!", "pos"),
("Either you're a liar, incompetent, or both. YOU SAID it would be American steel. You said it. Your word means nothing.", "pos"),
("HAHA. Typical Trump fan. Thinks Orange Mussolini has honest intentions. LOL.", "pos"),
("no we didn't, snowflake. We won. Big league.", "pos"),
("congrats - your hair color now matches the drapes", "neg"),
("you are going to make about 70 permanent jobs. Obama made 250K a month for 7 years straight. How does it feel? Sad.", "pos"),
("I see 12 white dudes and 1 orange clown.", "pos"),
("he's a fucking Russian puppet", "pos"),
("I long for the day you make your final announcement... your resignation.", "pos"),
("Inferior Lifeforms", "pos"),
("How r u 2day?", "neg"),
("Thanks to toby teardoopey from /r/h3h3productions for making questionable life decisions in honor of us", "neg"),
("Just want to say thank you to everyone for all the love and support! Feeling a lot better and truly blessed to have so much support  💕", "neg"),
("I'm that creepy guy that has portraits of himself in his house", "neg"),
("10 rappers who have actually KILLED people", "neg"),
("YOU HAVE FOUR FUCKING Ms IN YOUR NAME PAL THAT'S WAY TOO MANY Ms", "pos"),
("not mad, disappointed. You degrade our President while I watch with my family. In turn you degrade us, a lot of Americans, RUDE", "pos"),
("would you like to ask @realDonaldTrump how to run the oscars next year, maybe then you would get things done right", "pos"),
("jimmy needs new material...hard to even watch these 2 min clips...try harder buddy", "pos"),
("only thing getting messy as all the Un-American,bias celebrities that can't have own beliefs. #pathetic", "pos"),
("if your intentions arent good + you dont genuinely care about me please just leave me alone im tired", "neg"),
("what a fucking joke lol", "pos"),
("i will not allow pineapple pizza slander on my TL u can all choke", "pos"),
("boys that wear thrasher are 0% personality", "neg"),
("delete this", "neg"),
("not to be dramatic or anything but i highkey wanna be annihilated", "pos"),
("WARNING: As a safety precaution please avoid large groups of the opposite sex while wearing your @Tempo_Storm merch.", "neg"),
("#BecomingLegendary requires heart, skill, innovation, and of course some sick Tempo Storm gear always helps. ;) http://store.tempostorm.com", "neg"),
("One last day of recovery today and I'll be back streaming regularly tomorrow!", "neg"),
("No shit Sherlock.", "pos")
]


# returns percent probability that the string is a hit
def get_prob_of_pos(string):
    prob_dist = cl.prob_classify(string)
    return str("Probability of \"" + string + "\" being pos (hit): " + str(round(prob_dist.prob("pos"), 2)))


# returns percent probability that the string is a miss
def get_prob_of_neg(string):
    prob_dist = cl.prob_classify(string)
    return str("Probability of \"" + string + "\" being neg (miss): " + str(round(prob_dist.prob("neg"), 2)))


# returns class that is more likely to be true (pos or neg)
def get_most_likely_class(string):
    prob_dist = cl.prob_classify(string)
    return str("\"" + string + "\" is most likely " + prob_dist.max())


# returns accuracy of predictions versus set of test data
def get_accuracy(test):
    return str("Accuracy of predictions on test data: " + str(cl.accuracy(test)))


# displays list of words that indicate class in order by largest to smallest ratios
def display_indicators(num):
    return cl.show_informative_features(num)


# replaces currently loaded training data with new data
def update_training_data(new_data):
    return cl.update(new_data)


cl = pickle.load(open("classifier.pickle", "rb"))
print(get_prob_of_pos("asshat"))
print(get_prob_of_neg("sorry"))
print(get_most_likely_class("beaner"))
print(display_indicators(5))
print(get_accuracy(test))

