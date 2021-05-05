from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

def createModel(input_data, output):
    model = Sequential()
    model.add(Dense(128, input_shape=(len(input_data[0]), ), activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(len(output[0]), activation="softmax"))

    return model