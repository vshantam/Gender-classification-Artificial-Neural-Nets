import math
import pandas as pd
import numpy as np
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
import keras
import h5py
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense


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
	print("\n\nThere are list of extracted values from ranges 0 - 3167 audio files consist of 12 fetures")
	print("\n\nPlease select from the above extracted data usng serial number as 0 - 3167 \n")
	resp = int(input("Please enter the number:"))
	print(dataset.iloc[:,:-1].values[resp])
	classifier = load_model("classifier/clf.h5py")
	print (classifier.predict(dataset.iloc[:,:-1].values[resp].reshape(-1,1).T))
	


