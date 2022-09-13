from SentenceAnalyzer import SentenceAnalyzer as SA
from WordAnalyzer import WordAnalyzer as WA
from ml.Trainer import PosTrainer
from GrammarDriver import GrammarWebDriver as GWDriver


sentence_pos_file = open('./resources/sentences_list', 'r', encoding='latin1')
sentence_pos_list = sentence_pos_file.readlines()
Test_Input = [sentence.split(':')[0] for sentence in sentence_pos_list]
Test_Output = [sentence.split(':')[1] for sentence in sentence_pos_list]

print("TestInput and output")
print(Test_Input)
print(Test_Output)
posTrainer = PosTrainer(Test_Input, Test_Output, None)
posTrainer.train()
print("working")   