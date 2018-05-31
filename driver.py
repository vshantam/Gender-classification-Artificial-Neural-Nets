#importing the libraries
import numpy as np
import os,sys
import pandas as pd
import math
import cmath
import re
from scipy.io import wavfile
from matplotlib import pyplot as plt
import time

#creating class for feature extraction
class Extract(object):

	def __init__(self):
		pass

	#creating classmethod for loading the data and extracting fetures
	@classmethod
	def load_data(self):
		#get current working directory
		owd = os.getcwd()

		#setting path to dataset
		self.path = str('Datasets/pygender/Train/AudioSet/')

		#list of categorical dataset
		listdata = os.listdir(self.path)

		print(listdata)
		#looping through different dataset for male and female
		for i in range(len(listdata)):

			#changing the directory
			os.chdir(self.path+str(listdata[i])+"/")
			print(listdata[i])

			#loading each audio file for fft transformation
			for i in os.listdir():
				samplerate, data = wavfile.read(i)
				print(data)

			#going back to default directory
			os.chdir(owd)

	#defing omega for FFT
	@classmethod
	def omega(self,p, q):
		return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

	#actual defination for Fast fourier Transformation (FFT)
	@classmethod
	def fft(signal):

		#length of the signal
		n = len(signal)
		if n == 1:
			return signal
		else:
			#splitting into even and odd set
			Feven = fft([signal[i] for i in range(0, n, 2)])
			Fodd = fft([signal[i] for i in range(1, n, 2)])

 		#combining the both list
		combined = [0] * n
		for m in range(n//2):
		combined[m] = Feven[m] + self.omega(n, -m) * Fodd[m]
		combined[m + n/2] = Feven[m] - self.omega(n, -m) * Fodd[m]
 		
		#returning while converting list to numpy array
		return np.array(combined)


if __name__ == '__main__':
	
	#creating an object
	obj = Extract()
	obj.load_data()

		
