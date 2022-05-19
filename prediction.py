import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle


def make_prediction(text):
    # loading
    with open('./tokenizer/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    max_length = 1000

    sequences = tokenizer.texts_to_sequences([text])
    train_sequence = pad_sequences(
        sequences, maxlen=max_length, value=0.0, padding='post')

    loaded_model = tf.keras.models.load_model('./saved_models')

    results = loaded_model.predict(train_sequence)
    # print(results)
    if results[0][0] > results[0][1]:
        return f'True news, {"{:.0%}".format(results[0][0])} certainty'
    elif results[0][1] > results[0][0]:
        return f'Fake news, {"{:.0%}".format(results[0][1])} certainty'
