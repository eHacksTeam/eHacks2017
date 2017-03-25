import tweepy, time, sys

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

for line in f:
    print(line)
    results = api.search(q=str(line), lang='en')
    for tweet in results:
        string = str(tweet.text.encode("utf-8"))[2:]
        string2 = str()
        for char in range(len(string)):
            if not string[char] in bad_chars:
                    string2 += string[char]
        writefile.write(string2)
        writefile.write("\n")
        print(string2)
        writefile.flush()
        time.sleep(0.5)
writefile.close()
