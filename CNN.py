#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.preprocessing import sequence
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalMaxPooling1D, Flatten, Conv1D, Dropout, Activation
from keras.preprocessing.text import Tokenizer

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os
import re
import string

# For reproducibility
from numpy.random import seed
seed(1)
tf.random.set_seed(2)


# In[2]:


if tf.test.is_gpu_available():
    # GPU
    BATCH_SIZE = 128 # Number of examples used in each iteration
    EPOCHS = 2 # Number of passes through entire dataset
    VOCAB_SIZE = 30000 # Size of vocabulary dictionary
    MAX_LEN = 500 # Max length of review (in words)
    EMBEDDING_DIM = 40 # Dimension of word embedding vector

# Hyperparams for CPU training
else:
    # CPU
    BATCH_SIZE = 32
    EPOCHS = 2
    VOCAB_SIZE = 20000
    MAX_LEN = 90
    EMBEDDING_DIM = 40


# In[3]:


LABELS = ['negative', 'positive','neutral']

# Load data
train = pd.read_csv('finalcsv.csv')  # EDIT WITH YOUR TRAIN FILE NAME
print("Train shape (rows, columns): ", train.shape)
train.head()
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')

def tokenize(s): 
    return re_tok.sub(r' \1 ', s).split()

# Plot sentence by lenght
plt.hist([len(tokenize(s)) for s in train['Tweet'].values], bins=50)
plt.title('Tokens per sentence')
plt.xlabel('Len (number of token)')
plt.ylabel('# samples')
plt.show()

tokenizer = Tokenizer(num_words=VOCAB_SIZE)
tokenizer.fit_on_texts(train['Tweet'].values)

x_train_seq = tokenizer.texts_to_sequences(train['Tweet'].values)

x_train = sequence.pad_sequences(x_train_seq, maxlen=MAX_LEN, padding="post", value=0)

y_train = train['Sentiment'].values


print('First sample before preprocessing: \n', train['Tweet'].values[0], '\n')
print('First sample after preprocessing: \n', x_train[0])



NUM_FILTERS = 250
KERNEL_SIZE = 3
HIDDEN_DIMS = 250

print('Build model...')
model = Sequential()


model.add(Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LEN))
model.add(Dropout(0.2))

model.add(Conv1D(NUM_FILTERS,
                 KERNEL_SIZE,
                 padding='valid',
                 activation='relu',
                 strides=1))

# we use max pooling:
model.add(GlobalMaxPooling1D())

# We add a vanilla hidden layer:
model.add(Dense(HIDDEN_DIMS))
model.add(Dropout(0.2))
model.add(Activation('relu'))

# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train,batch_size=BATCH_SIZE,epochs=EPOCHS,validation_split=0.1,verbose=1)

score, acc = model.evaluate(x_train, y_train, batch_size=BATCH_SIZE)
print('\nAccuracy: ', acc*100)
pred = model.predict_classes(x_train)

model.save('D:/CMTSA/CodeMix')

model = tf.keras.models.load_model('D:/CMTSA/CodeMix')




