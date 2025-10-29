word = input().strip()
dial = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9,
}

total = 0

for ch in word:
    for key, value in dial.items():
        if ch in key:
            total += value + 1
            break

print(total)
