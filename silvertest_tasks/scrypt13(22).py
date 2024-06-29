word = input()
new_word = ''
for i in range(len(word) -1, -1, -1):
    new_word += word[i]
if word == new_word:
    print("YES")
else:
    print("NO")
    for s, l in zip(range(len(word)), range(len(new_word))):
        if word[s] != new_word[l]:
            print(s)
            break