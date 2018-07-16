"""
@author: Shantam Vijayputra
"""

import math
import pandas as pd
import numpy as np
import sys,os
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
import keras
import h5py
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':

	print(__doc__)

	#Ascii art 
	init(strip=not sys.stdout.isatty())
	cprint(figlet_format('G D S!', font='starwars'), 'green', 'on_red', attrs=['bold'])
	print("Gender Detection System !")
	print()
	print("Here are the list of extracted fetures from the audio files available in the database!")
	dataset = pd.read_csv("Datasets/voicegender(kaggle-extracted-dataset)/voice.csv")
	print(dataset.iloc[:,:-1].values)

	while True:
		print("\n\nThere are list of extracted values from ranges 0 - 3167 audio files consist of 12 fetures")
		print("\n\nPlease select from the above extracted data usng serial number as 0 - 3167 \n")
		resp = int(input("Please enter the number:"))
		print(dataset.iloc[:,:-1].values[resp])
		classifier = load_model("classifier/clf.h5py")
		scaler = StandardScaler()
		datas = (dataset.iloc[:,:-1].values[resp].reshape(-1,1).T)
		res = (classifier.predict(datas))
		print(res)
		if res > 4.3*10**-6 :
			print("Predicted Gender is : {}".format("Female"))
		else:
			print("Predicted Gender is : Male")
	
		print("The actual gender is : {}".format(dataset.iloc[:, -1].values[resp]))

	


