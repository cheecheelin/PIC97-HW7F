import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
from scipy import fftpack 
from scipy.fftpack import fft, ifft

#read audio samples
# sig= read("wooguy.wav")
rate, data = read('wooguy.wav') # load the data
# print data 
a = data.T[0] # get the first track of 2 channel soundtrack
# b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(a) # calculate fourier transform (complex numbers list)
d = len(c)/2  # half of the fft list (real signal symmetry)

print c 

c[9000:9300] = 0
c[-9300:-9000] = 0


e= ifft(c)
write('test.wav',rate,e.astype(data.dtype))


# plt.plot(abs(c[:(d-1)]),'r') 
plt.plot(abs(c[:(d-1)]),'r')
plt.show()








# 