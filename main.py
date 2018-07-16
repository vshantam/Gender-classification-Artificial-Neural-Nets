"""
@author: Shantam Vijayputra
"""

import math
import pandas as pd
import numpy as np
import sys,os
from colorama import init
from termcolor import cprint
import termcolor
from pyfiglet import figlet_format
import keras
import h5py
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler

def prCyan(skk):
	print("\033[96m {}\033[00m" .format(skk))

def prRed(skk):
	print("\033[91m {}\033[00m" .format(skk))

if __name__ == '__main__':

	os.system("reset")

	print(__doc__)

	#Ascii art 
	init(strip=not sys.stdout.isatty())
	cprint(figlet_format('G D S!', font='starwars'), 'blue', 'on_red', attrs=['bold'])
	print("Gender Detection System !")
	print()
	print(termcolor.colored("Here are the list of extracted features from the audio files available in the database!\n\n","red","on_white"))
	dataset = pd.read_csv("Datasets/voicegender(kaggle-extracted-dataset)/voice.csv")
	print(dataset.iloc[:,:-1].values)

	while True:

		prCyan("\n\nThere are list of extracted values from ranges 0 - 3167 audio files consist of 12 fetures")
		print("\n\nPlease select from the above extracted data usng serial number as 0 - 3167 \n")
		prRed("Please enter the number:")
		resp = int(input())
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

	


