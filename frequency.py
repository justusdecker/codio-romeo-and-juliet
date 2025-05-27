from romeo_and_juliet import PLAY
def getWords(text):
  counting = {}
  for line in text.split("\n"):
    for word in line.split(" "):
      if word == "": continue
      if word not in counting:
        counting[word] = 0
      else:
        counting[word] += 1
  return counting

def bubbleSort(array1,array2):
    
    n = len(array1)

    for i in range(n):
        for j in range(0, n - i - 1):

            if array1[j] > array1[j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
                array2[j], array2[j + 1] = array2[j + 1], array2[j]
    array1.reverse()
    array2.reverse()
    return array1,array2
if __name__ == "__main__":
  counting = getWords(PLAY)

  freqs, words = [counting[i] for i in counting], [i for i in counting]
  bs = bubbleSort(freqs,words)
  for i in range(50):
    print(f"{bs[1][i]:<10}: {bs[0][i]}")

