import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

class SarcasmModel : 

    def __init__(self) :
        self.model = self.get_model()
        self.tokenizer = self.get_tokenizer()
        self.max_length = 15
        self.max_words = 20000


    def get_model(self) :
        model = tf.keras.Sequential([
                                tf.keras.layers.Embedding(self.max_words, 64, input_length=self.max_length),
                                tf.keras.layers.GlobalAveragePooling1D(),
                                tf.keras.layers.Dense(64, activation='relu'),
                                tf.keras.layers.Dense(64, activation='relu'),
                                tf.keras.layers.Dense(16, activation='relu'),
                                tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.load_weights('./model1/checkpoint')
        return model

    
    def get_tokenizer(self) :
        with open('model1/tokenizer.pickle', 'rb') as handle:
            b = pickle.load(handle)
            return b


    def preprocess(self, sentence) :
        sequences = self.tokenizer.texts_to_sequences([sentence])
        padded = pad_sequences(sequences, maxlen=self.max_length, padding='post', truncating='post')

        return padded

    
    def get_sarcasm(self, sentence) : 
        padded = self.preprocess(sentence)
        result = self.model.predict(padded)

        if result>0.5 :
            return True, result
        else :
            return False, result