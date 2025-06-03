from romeo_and_juliet import PLAY

def get_words_frequency(word_array: list[str]) -> list[str]:
    """ count all words of a given list """
    counting = {}
    for word in word_array:
        if word:
            word = word.lstrip()
        
            if word not in counting:
                counting[word] = 1
            else:
                counting[word] += 1
    return counting

def get_words(text: str):
    """ Convert words to a list. """
    return [word.replace('\n','') for word in text.split(" ")]

def top_n_words(freq: dict[str,int],n: int):
    """ prints the top ``n`` words """
    words = [(freq[i],i) for i in freq]
    sorted_words = sorted(words, key = lambda w: w[0],reverse = True)
    for i in range(n):
        print(f"{str(sorted_words[i][1]):<10}: {str(sorted_words[i][0])}")
        
def main() -> None:
    """ All of the logic will be called from here"""
    words = get_words(PLAY)
    counting = get_words_frequency(words)
    top_n_words(counting,6)

if __name__ == "__main__":
    main()