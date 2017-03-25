from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import string


train = []
test = [] # needs test data
file = open("./traindata.txt", 'r')
lines = file.readlines()
for line in lines:
    temp = line.split(",")
    train.append( (temp[0],temp[1]) )
cl = NaiveBayesClassifier(train)
file.close()

blob = TextBlob("I don't like this thing. This thing doesn't like me.")

def main():
    
    for item in struct:
        print(item)


# returns percent probability that the string is a hit
def get_prob_of_pos(string):
    prob_dist = cl.prob_classify(string)
    return 100*round(prob_dist.prob("pos"), 2)


# returns percent probability that the string is a miss
def get_prob_of_neg(string):
    prob_dist = cl.prob_classify(string)
    return 100*round(prob_dist.prob("neg"), 2)


# returns class that is more likely to be true (pos or neg)
def get_most_likely_class(string):
    prob_dist = cl.prob_classify(string)
    return prob_dist.max()


# returns struct containing multiple sentences and classifications taken from a single TextBlob
def get_class_of_sents_in_blob(blob):
    struct = {}
    for s in blob.sentences:
        struct.append(s)
        struct.append(s.classify())
    return struct

#struct = get_class_of_sents_in_blob(blob)

# returns accuracy of predictions versus set of test data
def get_accuracy(test):
    return cl.accuracy(test)


# displays list of words that indicate class in order by largest to smallest ratios
def display_indicators(num):
    return cl.show_informative_features(num)


# replaces currently loaded training data with new data
def update_training_data(new_data):
    return cl.update(new_data)

if __name__ == "__main__":
    main()
