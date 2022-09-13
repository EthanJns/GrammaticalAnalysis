from SentenceAnalyzer import SentenceAnalyzer as SA
from WordAnalyzer import WordAnalyzer as WA
from ml.Trainer import PosTrainer
from GrammarDriver import GrammarWebDriver as GWDriver

# words_file = open('./resources/wordlist.txt', 'r', encoding='latin1')
pos_file = open('./resources/pos.txt', 'r', encoding='latin1')
pos_copy = open('./resources/pos_copy.txt', 'w+', encoding='latin1')
pos_copy_dict = {}
for line in pos_file.readlines():
    key = line.split(':')[0]
    val = line.split(':')[1]
    pos_copy_dict[key] = val

for key in pos_copy_dict:
    pos_copy.write(key+':'+pos_copy_dict[key])
# word_analyzer = WA()
# word_analyzer.analyze_file_batch(words_file, pos_file)
# sentence_pos_file = open('./resources/sentences_list', 'r', encoding='latin1')
# sentence_pos_list = sentence_pos_file.readlines()
# Test_Input = [sentence.split(':')[0] for sentence in sentence_pos_list]
# Test_Output = [sentence.split(':')[1] for sentence in sentence_pos_list]


# print("TestInput and output")
# print(Test_Input)
# print(Test_Output)
# posTrainer = PosTrainer(Test_Input, Test_Output, None)
# posTrainer.train()
print("working")   