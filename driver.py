import numpy as np
import os,sys
import pandas as pd
import math
import cmath
import re
from scipy.io import wavfile
from matplotlib import pyplot as plt
import time

class Extract(object):

	def __init__(self):

		pass

	@classmethod
	def load_data(self):
		owd = os.getcwd()
		self.path = str('Datasets/pygender/Train/AudioSet/')
		listdata = os.listdir(self.path)
		print(listdata)
		for i in range(len(listdata)):
			os.chdir(self.path+str(listdata[i])+"/")
			print(listdata[i])
			for i in os.listdir():
				samplerate, data = wavfile.read(i)
				print(data)
			os.chdir(owd)

	@classmethod
	def omega(self,p, q):
		return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

	@classmethod
	def fft(signal):
		n = len(signal)
		if n == 1:
			return signal
		else:
			Feven = fft([signal[i] for i in range(0, n, 2)])
			Fodd = fft([signal[i] for i in range(1, n, 2)])
 
		combined = [0] * n
		for m in range(n//2):
		combined[m] = Feven[m] + self.omega(n, -m) * Fodd[m]
		combined[m + n/2] = Feven[m] - self.omega(n, -m) * Fodd[m]
 
		return np.array(combined)


if __name__ == '__main__':
	
	obj = Extract()
	obj.load_data()

		
