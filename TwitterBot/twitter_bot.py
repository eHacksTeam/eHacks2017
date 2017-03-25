import tweepy, time, re
from nltk.tokenize import word_tokenize

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

argfile = "input.txt"
argfile2 = "output.txt"

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'fcThscxsJM0QI4myazCTjPIRc'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'BWZQA7NmZA6Ypf8ptIN6MIa1deSX8W4hVj8PlhnjIEjasTCNio'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '845541669370023936-RFA65KEuv8cO3Xt0Ek9rJEkXrKCyu2a'  # keep the quotes, replace this with your access token
ACCESS_SECRET = 'aMRRjxU1ExVceX40fFN9lGOiJkCIzBqx1YPwL0ZG5Cjox'  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()

writefile = open(argfile2, 'w')
bad_chars = ['<', '>', ';', ':', '@', '#', '$', '%', '^', '&', '*', '[', ']', '{' '}', '`', '~', '\\', '/', '|']


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


def concatenate_and_format_tokens(tokens):
    string = ""
    for i in range(len(tokens)):
        string += ' ' + tokens[i]
    string = "('" + string + "', ),"
    return string


for line in f:
    print(line)
    results = api.search(q=str(line), lang='en')
    for tweet in results:
        tokens = preprocess(str(tweet.text))
        """
        string = str(tweet.text.encode("utf-8"))[1:]
        string2 = str()
        for char in range(len(string)):
            if char is '\n' or char is '\t':
                string2 += ' '
            if not string[char] in bad_chars: #need exceptions for newline and tabs
                    string2 += string[char]
        """
        writefile.write(concatenate_and_format_tokens(tokens))
        writefile.write("\n")
        print(tokens)
        writefile.flush()
        time.sleep(0.5)
writefile.close()
