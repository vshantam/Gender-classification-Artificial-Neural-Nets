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
import statistics
from scipy.stats.mstats import gmean
from scipy.stats import kurtosis, skew, entropy

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
		f = open(owd+"/data.csv", "a+")

		print(listdata)
		#looping through different dataset for male and female
		for i in range(len(listdata)):

			#changing the directory
			os.chdir(self.path+str(listdata[i])+"/")
			print(listdata[i])

			#loading each audio file for fft transformation
			for j in os.listdir():

				print(j)
				samplerate, data = wavfile.read(j)
				data = scipy.fftpack.fft(data)
				data = abs(data)
				frequency = self.freqcalc(data, samplerate)
				meanfreq = abs(frequency.mean())
				meanstd = self.std(data)
				med = self.median(data)
				try:
					mode = statistics.mode(data)
				except Exception as e:
					mode = 0.0
				q75, q25, iqr = self.quart(data)
				kurtosis, skew, entropy = self.kurtskew(data)
				sfm = self.specflat(data)
				centroid = np.sum(data*frequency) / np.sum(data)				
				f.write(str(meanfreq));f.write(",")
				f.write(str(meanstd));f.write(",")
				f.write(str(med));f.write(",")
				f.write(str(mode));f.write(",")
				f.write(str(q75));f.write(",");f.write(str(q25));f.write(",");f.write(str(iqr));f.write(",")
				f.write(str(kurtosis));f.write(",");f.write(str(skew));f.write(",");f.write(str(entropy));f.write(",")
				f.write(str(sfm));f.write(",")
				f.write(str(centroid));f.write(",")
				if listdata[i] == "female_clips":
					f.write("female");f.write("\n")
				else:
					f.write("male");f.write("\n");

			#going back to default directory
			os.chdir(owd)

	#centriod frequency
	@classmethod
	def spectral_centroid(self, x, frequency):
		freqs = np.abs(self.fft(length, 1.0/samplerate)[:length//2+1]) # positive frequencies	np.fft.fftfreq	
		return np.sum(x*frequency) / np.sum(data) # return weighted mean

	#calculate spectral flatness
	@classmethod
	def specflat(self,data):
	
		res = gmean(data**2)/np.mean(data**2)
		
		return abs(res)

	#kurtosis and skew
	@classmethod
	def kurtskew(self,data):

		return kurtosis(data), skew(data), entropy(data)

	#calculating quartile
	@classmethod
	def quart(self,data):

		q75, q25 = np.percentile(data, [75,25])
		
		return q75, q25, (q75-q25)

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
		freqs = self.fft(data.size, t[1]-t[0])  #scipy.fftpack.fftfreq
	
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


