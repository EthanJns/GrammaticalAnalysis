from SentenceAnalyzer import SentenceAnalyzer as SA
from WordAnalyzer import WordAnalyzer as WA


#Open the POS file containing words and their parts of speech
#Open the 10 common sentences text file and store each sentence in a list, removing any punctuation
#Iterate over that list using the POS_Dictionary to create a version of the sentence that is only parts of speech 
word_list_file = open('./resources/test.txt', 'r', encoding='latin1')
pos_test_file = open('./resources/pos_test.txt','w', encoding='latin1')    #Open Pos File 
sentences_file = open('./resources/10_common_english_sentences.txt','r')
wa = WA()
wa.analyze_file_batch(word_list_file, pos_test_file)
# sa = SA(wa,pos_test_file)
# sa.analyze_text(sentences_file)
print("working")   