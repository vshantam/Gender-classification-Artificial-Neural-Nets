# Grender-classification-Artificial-Neural-Nets

This classifiers the gender of the person speaking in the singular audio file using Artificial Neural Networks

<b> Audio </b>       
         
![alt_tag](rgif.gif)

<b> Male/Female </b>

# Project Structure

    1.Introduction and Papers.
    2.Approches
    3.Data collection and Preprocessing
    4.signal Transformation
    5.Feature Extraction and visualisation
    6.Training
    7.Testing
    8.Evaluation
    9.Output
    10.References
    
# 1. Introduction

This project uses a mathamatical approach to determine the gender of the person speaking in the audio file .the implementation focusses more on the audio that consist the voice of a single person speaking at a time.As we know that directly we cannot use the audio data because it may consist some noise and other factors that we may not want to use.

To make our work easier we will be using the algorithm called <b> Fast Fourier Transformation (FFT) </b> . this technique will help us to extract better <b>quality of features</b> and those features will be using to train the classification model using Deep Neural Networks method called <b> Artificial Neural Networks</b>

## Papers 

The papers which we will be going to focus more are :

	1.Gender Classification in Speech Recognition using Fuzzy Logic and Neural Network # 3rd paper in the papers dataset
	2.Musical Genre Classification of Audio Signals # 4th paper from the IEEE Papers dataset


# 2.Approches

The steps that we are going to take to build the model are as follows:

	1. Load the audio file.
	2. Transform the audio signal using FFT.
	3. Extract meaningful features.
	4. create the dataset.
	5. cleaning the dataset.
	6. scaling the dataset.
	7. Building Neural Nets.
	8. Training the model.
	9. Accuracy calculation.
	10.Performance tuning.
	11.Deploying the Model.

# 3.Data collection and Preprocessing

I have uploaded the dataset that i used in the dataset forlder which contains two types of data.The first type of data is the actual audio data nad the second type of data is the the csv data whch contains the extracted features from real audio data.
I will be shuffleing both the data after extraction of features.

# 4.Signal Transformation

Initially the data dataset contains all the audio files, so we need to transform each audio file in the folder using <B> FFT </B>.

FFT IMPLEMENTATION IN PYTHON3

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

 			
			combined = [0] * n #combining the both list
			for m in range(n//2):
				combined[m] = Feven[m] + self.omega(n, -m) * Fodd[m]
				combined[m + n//2] = Feven[m] - self.omega(n, -m) * Fodd[m]
 			
			#returning while converting list to numpy array
			return np.array(combined)


<b> sample audio plotting :</b>

<b> Male vs Female </b>

![alt_tag](Figures/audio.png)

<b> Male vs Female </b>

<b> sample audio plotting after transformation: </b>

![alt_tag](Figures/audio_trans.png)


# 5.Feature Extraction and visualisation

The List of MFCC Features which i will be using are as follows :

	1.Mean Frequency
	2.Standard Devation
	3.Median
	4.Third Quartile (Q75)
	5.First Quartile(Q25)
	6.Inter Quartile(IQR)
	7.Skewness
	8.Kurtosis
	9.Spectral Entropy
	10.Spectral Flatness
	11.Mode
	12.Central Frequency


	Q.What is MFCC ?

	Ans:-Mel-frequency cepstral coefficients (MFCCs) are coefficients that collectively make up an MFC.
	They are derived from a type of cepstral representation of the audio clip (a nonlinear "spectrum-of-
	a-spectrum").

References Used :

<b>“The International Arab Journal of Information Technology, Vol. 10, No. 5, September 2013”</b>

## Dataset Snapshot

![alt_tag](Figures/dataset.png)

## Extracted Feature

![alt_tag](Figures/Features.png)

## Visualization

![alt_tag](Figures/meanfreq.png)

![alt_tag](Figures/median.png)

![alt_tag](Figures/Q75.png)

![alt_tag](Figures/Q25.png)

![alt_tag](Figures/IQR.png)

![alt_tag](Figures/mode.png)

![alt_tag](Figures/sd.png)

![alt_tag](Figures/kurt.png)

![alt_tag](Figures/sfm.png)

![alt_tag](Figures/skew.png)

![alt_tag](Figures/sp.ent.png)

![alt_tag](Figures/centroid.png)

# 6. Training

Using Artifcial Neural Network to train the model for classification problem because Neural Nets seems to give the most accurate results in terms of accuracy.

![alt_tag](Figures/ann.png)


The description of the architecture i am using for classification are as follows:

	1. 1 input layer , Hidden layer, 1 Output Layer.
	2. using 12 input attributes and 1 output attributes.
	3. activation function for input and hidden layer is “relu”.
	4. activation function for output layer is “sigmoid”.
	5. using 10 perceptron in each input and hidden layer.
	6. for optimisation algorthm is used “adam”.



<B>Q. What is Perceptron?</B>

<B>Ans :</B>

a computer model or computerized machine devised to represent or simulate the ability of the brain to recognize and discriminate.

![alt_tag](Figures/sl_perceptron.png)

<b>
Q.What is activation Function?

Ans : 
</b>

In artificial neural networks, the activation function of a node defines the output of that node given an input or set of inputs. A standard computer chip circuit can be seen as a digital network of activation functions that can be "ON" (1) or "OFF" (0), depending on input.

<b>ReLu activation Function:</b>

A unit employing the rectifier is also called a rectified linear unit (ReLU).
A smooth approximation to the rectifier is the analytic function

<b> F(x) = Log(1 + exp(x)) </b>

which is called the softplus function

Sigmoid activaton Function:

It is used in neural networks to give logistic neurons real-valued output that is a smooth and bounded function of their total input. It also has the added benefit of having nice derivatives which make learning the weights of a neural network easier.

<b>	F(x) = 1/ (1 + exp(-x)) </b>


<b>Graphical Representation</b>

![alt_tag](Figures/sigmoidvsrelu.png)

<b>Implementation</b>


## Modules used:

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


<b>Using python keras module for layer creation and compilation:</b>

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

## Learnng Curve:

![alt_tag](Figures/learning_curve.png)


