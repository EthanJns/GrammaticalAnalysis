from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

#The following class will be used to tokenize/vectorize out data
class PosTokenizer:
    def __init__():
        print("This class will be used to tokenize sentences into parets of speech into vectorized data for our nn")

    def vectorize_input_data(self, sentences):
        vocab_size, max_length = self.get_vocab_size_max_len(sentences)
        encoded_sentences = [one_hot(d, vocab_size) for d in sentences]
        padded_sentences = pad_sequences(encoded_sentences, maxlen=max_length, padding='post')

        return padded_sentences

    def get_vocab_size_max_len(self, sentences):
        max_size = 0
        word_set = set()
        for sentence in sentences:
            sentence_as_list = sentence.split(' ')
            max_size = len(sentence_as_list) if len(sentence_as_list) > max_size else max_size
            word_set.update(sentence_as_list)
        
        return len(word_set), max_size
        