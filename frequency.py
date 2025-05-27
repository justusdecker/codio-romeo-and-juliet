from romeo_and_juliet import PLAY

def getWords(text):
    counting = {}
    for line in text.split("\n"):
        for word in line.split(" "):
            if word == "": continue
        if word not in counting:
            counting[word] = 1 # fixed logic issue
        else:
            counting[word] += 1
    return counting

if __name__ == "__main__":
    counting = getWords(PLAY)

    words = [(counting[i],i) for i in counting]
    sorted_words = sorted(words, key = lambda w: w[0],reverse = True)
    for i in range(50):
        print(f"{str(sorted_words[i][1]):<10}: {str(sorted_words[i][0])}")

