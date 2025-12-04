import string

msg = input()
cnts = {c: 0 for c in string.ascii_uppercase}
odd, idx, mid_used = 0, 0, False
res = [""] * len(msg)

for ch in msg:
    cnts[ch] += 1

odd = sum(cnts[c] % 2 for c in string.ascii_uppercase)
if odd > 1:
    print("I'm Sorry Hansoo")
    exit()

for c in string.ascii_uppercase:
    cnt = cnts[c]

    while cnt >= 2:
        res[idx] = res[-idx-1] = c
        idx += 1
        cnt -= 2

    if cnt == 1 and not mid_used:
        res[len(msg) // 2] = c
        mid_used = True

print("".join(res))
