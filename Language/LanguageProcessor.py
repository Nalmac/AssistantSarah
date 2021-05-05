import os
import keras
from keras.models import load_model
from Models.Brain import createModel
from Language.Trainer import Trainer
import numpy as np
import pandas as pd
import nltk

class LanguageProcessor():
    def __init__(self):
        self.trainer = Trainer()
        if os.path.isfile("./Language/model_trained.h5"):
            self.model = load_model("./Language/model_trained.h5")
        else:
            self.model = self.trainer.trainModel()
    
    def clean_up_sentence(self, text):
        sentence_words = nltk.word_tokenize(text)
        sentence_words = [self.trainer.stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words
    
    def bow(self, sentence, words, show_details=True):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0]*len(words)  
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s: 
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))
    
    def processText(self, text):
        ERROR_THRESHOLD = 0.25
        input_data = pd.DataFrame([self.bow(text, self.trainer.words)], dtype=float, index=['input'])
        results = self.model.predict([input_data])[0]
        results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return [(self.trainer.classes[r[0]], str(r[1])) for r in results]