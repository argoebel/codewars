def order(sentence):
    orderedSentence = [""] * len(sentence.split(" "))
    for word in sentence.split(" "):
        for i in word:
            if i.isnumeric():
                orderedSentence[int(i)-1] = word
                break
    return " ".join(orderedSentence)

def order_best(words):
  return ' '.join(sorted(words.split(" "), key=lambda w:sorted(w)))

print(order_best("is2 Thi1s T4est 3a"))
print(order_best(""))
