import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

class Prep(object):

	#loading dataset
	@classmethod
	def load(self,path):
		self.df = pd.read_csv(path, engine = "python", sep = ",")

		return self.df

	#dealing with missing values
	@classmethod
	def nanval(self):
		if (self.df.isnull().values.any()) == True:
			null_columns=train.columns[train.isnull().any()]
			for i in null_columns:
				self.df[i] = self.df[i].fillna(self.df[i].mean())
		return self.df

	#encoding the dataset
	@classmethod
	def encoding(self):
		self.x = self.df.iloc[:,:-1].values
		self.y = self.df.iloc[:,-1].values
		le = preprocessing.LabelEncoder()
		self.y = le.fit_transform(self.y)

		return self.x, self.y
		

	#saving preprocessed data
	@classmethod
	def savedata(self,x, y):
		np.savetxt("PreProcessed_Data/input.csv",x,delimiter=",")
		np.savetxt("PreProcessed_Data/output.csv",y,delimiter=",")

	#visualization
	@classmethod
	def plot_viz(self):
		df = self.df
		maledf = df.loc[df['label'] == "male"] 
		femaledf = df.loc[df['label'] == "female"]
		name = df.columns

		for i in name[:-1]:

			plt.subplot(211)
			plt.hist(maledf[i],label = "male", color = "green")
			plt.legend(loc = "upper right")
			plt.subplot(212)
			plt.hist(femaledf[i],label="female", color= "orange")
			plt.legend(loc = "upper right")
			plt.suptitle("{} variation of male and female".format(i))
			plt.savefig("Figures/"+str(i)+".png")

if __name__ == "__main__":

	obj = Prep()
	df = obj.load("Datasets/voicegender(kaggle-extracted-dataset)/voice.csv")
	df = obj.nanval()
	x, y = obj.encoding()
	scaler = MinMaxScaler()
	x = scaler.fit_transform(x)
	obj.savedata(x,y)
	obj.plot_viz()

