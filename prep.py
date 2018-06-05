import numpy as np
import pandas as pd
from sklearn import preprocessing

class Prep(object):

	#loading dataset
	@classmethod
	def load(self,path):
		self.df = pd.read_csv(path, engine = "python", header = None, sep = ",")

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
		self.x = self.df.iloc[:,:-1].values()
		self.y = self.df.iloc[:,-1].values()
		le = preprocessing.LabelEncoder()
		self.y = le.fit_transform(self.y)

		return self.x, self,y
		


if __name__ == "__main__":

	obj = Prep()
	df = obj.load("Datasets/voicegender(kaggle-extracted-dataset)/voice.csv")
	df = obj.nanval()
	x, y = obj.encoding()
	
