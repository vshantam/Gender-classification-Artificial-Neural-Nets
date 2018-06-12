import numpy as np
import pandas as pd
import h5py
from sklearn.model_selection import train_test_split
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout, LeakyReLU, BatchNormalization


class Train(object):

	#load_dataset
	@classmethod
	def load(self, path_x, path_y):
		self.x = pd.read_csv(path_x, engine="python")
		self.y = pd.read_csv(path_y, engine="python")
		return self.x, self.y

	#split train and test data
	@classmethod
	def split_data(self):
		self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x,self.y, test_size=0.33, random_state=42)
		return self.x_train, self.x_test, self.y_train, self.y_test

	#creating model
	@classmethod
	def create_model(self):
		self.model = Sequential()

		self.model.add(Dense(64, input_dim=12, init='uniform'))
		self.model.add(LeakyReLU(alpha=0.3))
		self.model.add(BatchNormalization(epsilon=1e-06, mode=0, momentum=0.9, weights=None))
		self.model.add(Dropout(0.5)) 

		self.model.add(Dense(64, init='uniform'))
		self.model.add(LeakyReLU(alpha=0.3))
		self.model.add(BatchNormalization(epsilon=1e-06, mode=0, momentum=0.9, weights=None))
		self.model.add(Dropout(0.5))


		self.model.add(Dense(64, init='uniform'))
		self.model.add(LeakyReLU(alpha=0.3))
		self.model.add(BatchNormalization(epsilon=1e-06, mode=0, momentum=0.9, weights=None))
		self.model.add(Dropout(0.5))

		self.model.add(Dense(64, init='uniform'))
		self.model.add(LeakyReLU(alpha=0.3))
		self.model.add(BatchNormalization(epsilon=1e-06, mode=0, momentum=0.9, weights=None))
		self.model.add(Dropout(0.5))


		self.model.add(Dense(1, init='uniform'))
		self.model.add(Activation('softmax'))
		return self.model

	#training
	@classmethod
	def train(self):
		self.model = create_model()
		sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
		self.model.compile(loss='binary_crossentropy', optimizer=sgd)
		self.model.fit(self.x_train, self.y_train, nb_epoch=20, batch_size=16, show_accuracy=True, validation_split=0.2, verbose=2)
		return self.model


	#saving trained model
	@classmethod
	def save_trained_model(self):
		self.model.save_weights("classifier/clf.h5py")

if __name__ == "__main__":

	obj = Train()
	x, y = obj.load("PreProcessed_Data/input.csv", "PreProcessed_Data/output.csv")
	x_train, x_test, y_train, y_test = obj.split_data()
	print(x_train)



