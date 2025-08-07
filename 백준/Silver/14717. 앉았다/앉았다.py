import sys
input = sys.stdin.readline
from itertools import combinations

matrix = []
win = 0

cards = []
for i in range(1, 11):
    cards += [i, i]

n = list(map(int, input().split()))
cards.remove(n[0])
cards.remove(n[1])
n.sort()

for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        matrix.append(sorted([cards[i], cards[j]]))

total = len(matrix)

def get_score(pair):
    if pair[0] == pair[1]: 
        return 100 + pair[0]
    return (pair[0] + pair[1]) % 10  

my_score = get_score(n)

i = 0
while i < total:
    opp = matrix[i]
    opp_score = get_score(opp)

    if my_score > opp_score:
        win += 1
    i += 1

print(f"{win/total:.3f}")
