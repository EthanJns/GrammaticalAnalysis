test_file = open('./resources/test.txt', 'r')
test_pos_file = open('./resources/pos_test.txt', 'r')

words = []
pos_words = []
for word in test_file.readlines():
    words.append(word.strip())
for word in test_pos_file.readlines():
    word = word.split(":")[0]
    pos_words.append(word.strip())
word_set = set(words)
pos_word_set = set(pos_words)

missing_words = []
for word in pos_word_set:
    if word in word_set:
        continue
    else:
        missing_words.append(word)
# print(len(words))
print("MISSING WORDS")
print(missing_words)