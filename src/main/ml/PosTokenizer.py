from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

#The following class will be used to tokenize/vectorize out data
class PosTokenizer:

    def __init__(self):
        self.one_hot_pos = {'noun':1, 'verb':2, 'adjective':3, 'adverb':4, 'article':5, 'preposition':6, 'conjunction':7, 'pronoun':8}

    def vectorize_input_data(self, sentences, vocab_size, max_length):
        encoded_sentences = [one_hot(d, vocab_size) for d in sentences]
        padded_sentences = pad_sequences(encoded_sentences, maxlen=max_length, padding='post')

        return padded_sentences 

    def vectorize_output_data(self, sentences, vocab_size, max_length):
        encoded_pos = []
        for sentence in sentences:
            pos_list = sentence.split(' ')
            pos_encoded = []
            for pos in pos_list:
                if pos in self.one_hot_pos:
                    pos_encoded.append(self.one_hot_pos[pos])
                else:
                    pos_encoded.append(0)
            encoded_pos.append(pos_encoded)
        padded_pos = pad_sequences(encoded_pos, maxlen=max_length, padding='post')

        return padded_pos

    def get_vocab_size_max_len(self, sentences):
        max_size = 0
        word_set = set()
        for sentence in sentences:
            sentence_as_list = sentence.split(' ')
            max_size = len(sentence_as_list) if len(sentence_as_list) > max_size else max_size
            word_set.update(sentence_as_list)
        
        return len(word_set), max_size
        