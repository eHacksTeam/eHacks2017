def grabNewFiles():
    file1 = open("output.txt")
    file2 = open("old_data.txt")
    return file1, file2


def giveFile():
    while True:
        file1, file2 = grabNewFiles()
        file3 = open("combinedData", "w")
        for line in file1:
            file3.write(file1.readline() + file2.readline())
    return file3
