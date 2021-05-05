import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
from keras.optimizers import SGD
import random
import json
import os
from Models.Brain import createModel

class Trainer():
    def __init__(self):
        self.stemmer = LancasterStemmer()
        self.words = json.load(open("./Language/words.json")) if os.path.isfile("./Language/words.json") else []
        self.classes = json.load(open("./Language/classes.json")) if os.path.isfile("./Language/classes.json") else []

    def processData(self):
        with open("./Language/intents.json") as file:
            data = json.load(file)

        documents = self.firstProcessing(data, [])

        out_empty = [0] * len(self.classes)

        training = self.secondProcessing(documents, out_empty, [])

        random.shuffle(training)
        training = np.array(training)

        train_x = list(training[:,0])
        train_y = list(training[:,1])

        json.dump(self.words, open("./Language/words.json","w"))
        json.dump(self.classes, open("./Language/classes.json","w"))
 
        return train_x, train_y

    def firstProcessing(self, data, documents):
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                self.words.extend(wrds)
                documents.append((wrds, intent['tag']))
            if intent["tag"] not in self.classes:
                self.classes.append(intent["tag"])

            self.words = [self.stemmer.stem(w.lower()) for w in self.words if w != "?"]
            self.words = sorted(list(set(self.words)))

            self.classes = sorted(list(set(self.classes)))
        return documents

    def secondProcessing(self, documents, out_empty, training):
        for doc in documents:
            bag = []
            pattern_words = doc[0]
            wrds = [self.stemmer.stem(w.lower()) for w in pattern_words]

            for w in self.words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)
            output_row = list(out_empty)
            output_row[self.classes.index(doc[1])] = 1

            training.append([bag, output_row])
        return training

    def trainModel(self):
        processed_data = self.processData()
        train_x, train_y = processed_data
        model = createModel(train_x, train_y)

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])
        model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
        model.save("./Language/model_trained.h5")
        return model
