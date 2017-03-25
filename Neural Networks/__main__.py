from textblob import TextBlob
import string


def main():
    file = open("../TwitterBot/output.txt", 'r')
    f = file.readlines()
    file.close()
    for line in f:
        for char in range(0, len(line)):
            if not line[char] in string.ascii_letters:
                line = line.replace(line[char], ".")
        line = line.replace('.', ' ')
        line = line[1:]
        #print(line)
        text = TextBlob(line)
        print(text+"\n")
        print(text.parse())

if __name__ == "__main__":
    main()
