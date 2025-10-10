import re

tokens = [t for t in re.split(r'(<|>|\s)', input()) if t]  # 공백도 토큰화
word = True  # 외부 단어 뒤집기 여부

for element in tokens:
    if element == "<":
        word = False
        print(element, end='')
    elif element == ">":
        word = True
        print(element, end='')
    elif element.isspace():
        print(element, end='')  # 공백은 그대로 출력
    else:
        print(element[::-1] if word else element, end='')
