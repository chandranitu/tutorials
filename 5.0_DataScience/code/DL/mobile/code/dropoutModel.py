def create_model():  
    # create model  
    model = Sequential()  
    model.add(Dropout(0.2, input_shape=(60,)))  
    model.add(Dense(60, activation='relu'))  
    model.add(Dense(1, activation='sigmoid'))  
    # Compile model  sgd = SGD(lr=0.1)  
    model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])  
    return model