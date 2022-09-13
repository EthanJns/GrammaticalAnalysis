from ml.PosModel import PosModel
from ml.PosTokenizer import PosTokenizer
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Embedding

class PosTrainer:

    def __init__(self, training_input, training_output, model_location, optimizer='sgd', loss_function='categorical_crossentropy'):
        self.model = PosModel(model_location)
        self.tokenizer = PosTokenizer()
        self.input, self.output = self.sanitize_input_output(training_input, training_output)
        self.optimizer = optimizer
        self.loss_function = loss_function

    def sanitize_input_output(self, input_data, output):
        sanitzied_input = [sentence.strip() for sentence in input_data]
        sanitzied_output = [sentence.strip() for sentence in output]
        return sanitzied_input, sanitzied_output

    def change_input(self, input_data):
        self.input = input_data
    
    def change_output(self, output_data):
        self.output = output_data
        
    def train(self):
        vocab_size, max_size = self.tokenizer.get_vocab_size_max_len(self.input)
        print("Vocab Size: {0}".format(vocab_size))
        print("Max Size: {0}".format(max_size))
        tokenized_input = self.tokenizer.vectorize_input_data(self.input, vocab_size, max_size)
        print("Tokenized_Input: ")
        print(tokenized_input)

        tokenized_output =  self.tokenizer.vectorize_output_data(self.output, vocab_size, max_size)
        print("Tokenized_Output: ")
        print(tokenized_output)

        if self.model.is_loaded:
            self.model.add_layer(Embedding(vocab_size, max_size*2, input_length=max_size, name='embedding'))
            self.model.add_layer(Flatten())
            self.model.add_layer(Dense(max_size, activation='sigmoid'))
            self.model.get_model().compile(optimizer=self.optimizer, loss=self.loss_function, metrics=['accuracy'])
            self.model.get_model().summary()

        self.model.get_model().fit(tokenized_input, tokenized_output, epochs=50, verbose=0)
        print(self.model.get_model().get_layer('embedding').get_weights()[0])