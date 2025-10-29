
from gettext import find


n = int(input())

while n != 0 :
    words = sum([list(map(str, input().split("\n"))) for _ in range(n)],[])
    lower_words = []
    sorted_word = []

    for el in words: 
        lower_words.append(el.lower())

    sorted_word = sorted(lower_words)
    print(words[lower_words.index(sorted_word[0])])

    n = int(input())

