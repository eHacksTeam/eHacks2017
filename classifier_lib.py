import pickle


# returns percent probability that the string is a hit
def get_prob_of_pos(string):
    prob_dist = cl.prob_classify(string)
    return round(prob_dist.prob("pos"), 2)


# returns percent probability that the string is a miss
def get_prob_of_neg(string):
    prob_dist = cl.prob_classify(string)
    return round(prob_dist.prob("neg"), 2)


# returns class that is more likely to be true (pos or neg)
def get_most_likely_class(string):
    prob_dist = cl.prob_classify(string)
    return prob_dist.max()


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
print("Probability of \"" + "asshat" + "\" being pos (hit): " + str(get_prob_of_pos("asshat")))
print("Probability of \"" + "sorry" + "\" being neg (miss): " + str(get_prob_of_neg("sorry")))
print("\"" + "beaner" + "\" is most likely " + get_most_likely_class("beaner"))
print(display_indicators(5))
file = open("output.txt", "r")
f = file.readlines()
num = 0
for line in f:
    print(line)
    if get_most_likely_class(line) is "pos":
        num += 1
        print("replaced " + num + " tags")
        line.replace("neg", "pos")
