import numpy as np
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras import models
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Embedding
from tensorflow.keras.losses import CategoricalCrossentropy

# Below will be a somewhat tutorial idea of what needs to happen

model = models.load_model('./ml/word_model')

Test_Sentences = ["The boy ran", "She is a girl", "It is in the shed", "What is that thing"]
sentiment = np.array([[1,2,3,0,0], [1,2,3,4,0], [1,2,3,4,5], [1,5,3,1,0]])
vocab_size = 30
encoded_sentences = [one_hot(d, vocab_size) for d in Test_Sentences]
print(encoded_sentences)

max_length = 5
padded_sentences = pad_sequences(encoded_sentences, maxlen=max_length, padding='post')
print(padded_sentences)

embeded_vector_size = 5
model = Sequential()
model.add(Embedding(vocab_size, embeded_vector_size, input_length=max_length, name='embedding'))
model.add(Flatten())
model.add(Dense(5, activation='sigmoid'))

X = padded_sentences
Y = sentiment

#I believe the loss is what we need to look into, since we will need values that are based on non binary outputs (1-8)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(X, Y, epochs=50, verbose=0)
print(model.get_layer('embedding').get_weights()[0])
# model.save('./ml/word_model')