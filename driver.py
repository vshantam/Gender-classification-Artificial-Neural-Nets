#importing the libraries
import numpy as np
import os,sys
import pandas as pd
import math
import cmath
import re
import scipy
from scipy import signal
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
		self.path = str('Datasets/pygender/Test/youtube/')

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
				print(i)
				samplerate, data = wavfile.read(i)
				data = np.fft.fft(data)
				data = abs(data)
				frequency = self.freqcalc(data, samplerate)
				meanfreq = abs(frequency.mean())
				meanstd = self.std(frequency)
				med = self.median(frequency)
				print(meanfreq, abs(meanstd), abs(med))
				
			#going back to default directory
			os.chdir(owd)

	#calculating median
	@classmethod
	def median(self, frequencies):
	
		return (np.median(frequencies))

	#calculating standard deviation
	@classmethod
	def std(self, frequencies):

		return (np.std(frequencies))

	#calculating frequency
	@classmethod
	def freqcalc(self, data, samplerate):

		N = data.shape[0]
		secs = N / float(samplerate)
		Ts = 1.0/samplerate # sampling interval in time
		t = scipy.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray
		freqs = scipy.fftpack.fftfreq(data.size, t[1]-t[0])
	
		return 	(freqs)

	#defining omega for FFT
	@classmethod
	def omega(self,p, q):
		return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

	#actual defination for Fast fourier Transformation (FFT)
	@classmethod
	def fft(self,signal):

		#length of the signal
		n = len(signal)
		if n == 1:
			return signal
		else:
			#splitting into even and odd set
			Feven = self.fft([signal[i] for i in range(0, n, 2)])
			Fodd = self.fft([signal[i] for i in range(1, n, 2)])

 		#combining the both list
		combined = [0] * n
		for m in range(n//2):
			combined[m] = Feven[m] + self.omega(n, -m) * Fodd[m]
			combined[m + n//2] = Feven[m] - self.omega(n, -m) * Fodd[m]
 		
		#returning while converting list to numpy array
		return np.array(combined)


if __name__ == '__main__':
	
	#creating an object
	obj = Extract()
	obj.load_data()

		
