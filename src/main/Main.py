from SentenceAnalyzer import SentenceAnalyzer as SA
from WordAnalyzer import WordAnalyzer as WA
from ml.Trainer import PosTrainer


#Open the POS file containing words and their parts of speech
#Open the 10 common sentences text file and store each sentence in a list, removing any punctuation
#Iterate over that list using the POS_Dictionary to create a version of the sentence that is only parts of speech 
word_list_file = open('./resources/test.txt', 'r', encoding='latin1')
pos_test_file = open('./resources/pos_test.txt','w', encoding='latin1')    #Open Pos File 
sentences_file = open('./resources/10_common_english_sentences.txt','r')
wa = WA()
wa.analyze_file_batch(word_list_file, pos_test_file)
pos_test_file = open('./resources/pos_test.txt','r', encoding='latin1')    #Open Pos File 
sa = SA(wa,pos_test_file)
sa.analyze_text(sentences_file)

sentence_pos_file = open('./resources/sentences_list', 'r', encoding='latin1')
sentence_pos_list = sentence_pos_file.readlines()
Test_Input = [sentence.split(':')[0] for sentence in sentence_pos_list]
Test_Output = [sentence.split(':')[1] for sentence in sentence_pos_list]
# Test_Input = ["The boy ran", "She is a girl", "It is in the shed", "What is that thing"]
# Test_Output = ['article noun verb', 'pronoun verb article noun', 'pronoun verb preposition article noun', 'pronoun verb pronoun noun']

# print("TestInput and output")
# print(Test_Input)
# print(Test_Output)

posTrainer = PosTrainer(Test_Input, Test_Output, None)
posTrainer.train()
print("working")   