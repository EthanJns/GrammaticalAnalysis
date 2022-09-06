from SentenceAnalyzer import SentenceAnalyzer as SA
from WordAnalyzer import WordAnalyzer as WA
print("Instanciating Sentence Analyzer")
sa = SA()
wa = WA()
print("Instanciated Main")
word_list_file = open('./resources/10_common_english_sentences.txt', 'r', encoding='latin1')
pos_file = open('./resources/pos.txt', 'w+' , encoding='latin1')
wa.analyze_file_batch(word_list_file, pos_file)