import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
from scipy import fftpack 
from scipy.fftpack import fft

#read audio samples
# sig= read("wooguy.wav")
fs, data = read('wooguy.wav') # load the data
print data 

a = data.T[0] # get the first track of 2 channel soundtrack

c = fft(a) # calculate fourier transform (complex numbers list)
d = len(c)/2  # half of the fft list (real signal symmetry)

c[np.abs(c) > 500] = 0
main_sig=fftpack.ifft(c)

# plt.plot(abs(c[:(d-1)]),'r') 
plt.plot(abs(c[:d]),'r')
plt.show()






# audio= sig[1]

# #plot the first 1000 samples
# plt.plot(audio[0:1000])

# #label axes 
# plt.ylabel("amplitude")
# plt.xlabel("frequency")

# plt.title("wooguy")

# plt.show()




# b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)