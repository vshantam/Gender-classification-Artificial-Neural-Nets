import numpy as np
import pandas as pd
import h5py
from sklearn.model_selection import train_test_split
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import optimizers
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


class Train(object):

	#load_dataset
	@classmethod
	def load(self, path_x, path_y):
		self.x = pd.read_csv(path_x, engine="python")
		self.y = pd.read_csv(path_y, engine="python")
		return self.x, self.y

	#shuffeling the data
	@classmethod
	def shuffle(self):
		self.x = shuffle(self.x, random_state=0)
		self.y = shuffle(self.y, random_state=0)
		return self.x, self.y

	#split train and test data
	@classmethod
	def split_data(self):
		self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x,self.y, test_size=0.33, random_state=0)
		return self.x_train, self.x_test, self.y_train, self.y_test



	#saving trained model
	@classmethod
	def save_trained_model(self, model):
		model.save_weights("classifier/clf.h5py")

if __name__ == "__main__":

	obj = Train()
	x, y = obj.load("PreProcessed_Data/input.csv", "PreProcessed_Data/output.csv")
	x, y = obj.shuffle()
	x_train, x_test, y_train, y_test = obj.split_data()

	# Initialising the ANN
	classifier = Sequential()
	
	# Adding the input layer and the first hidden layer
	classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu', input_dim = 12))
	
	# Adding the second hidden layer
	classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu'))
	
	# Adding the third hidden layer
	classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu'))
	
	# Adding the output layer
	classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))
	
	# Compiling the ANN
	classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
	
	# Fitting the ANN to the Training set
	history = classifier.fit(x_train, y_train, batch_size = 20, nb_epoch = 200)
	
	obj.save_trained_model(classifier)

	plt.title("loss vs accuracy curve")

	plt.ylabel("loss")
	
	plt.xlabel("accuracy")

	plt.plot(history.history['acc'], history.history['loss'], label = "learning curve")
	
	plt.legend(loc = "upper right")

	plt.show()


	# Predicting the Test set results
	y_pred = classifier.predict(x_test)
	y_pred = (y_pred > 0.5)
	
	# Making the Confusion Matrix
	cm = confusion_matrix(y_test, y_pred)

	print(cm)

