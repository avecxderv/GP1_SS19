#Fouriertransoformationen
plt.subplot(2,1,1)
fourier = analyse.fourier_fft(timeVal,voltage)
frequency = fourier[0]
amplitude = fourier[1]
plt.plot(frequency, amplitude)
plt.grid()
plt.xlabel('Frequenz / Hz')
plt.ylabel('Amplitude')

maximumIndex = amplitude.argmax();
plt.xlim(frequency[max(0, maximumIndex-10)], frequency[min(maximumIndex+10, len(frequency))])
peak = analyse.peakfinder_schwerpunkt(frequency, amplitude)
plt.axvline(peak)

plt.subplot(2,1,2)
fourier2 = analyse.fourier_fft(timeVal, voltage2)
frequency2 = fourier2[0]
amplitude2 = fourier2[1]
plt.plot(frequency2, amplitude2)
plt.grid()
plt.xlabel('Frequenz / Hz')
plt.ylabel('Amplitude')

maximumIndex = amplitude2.argmax();
plt.xlim(frequency2[max(0, maximumIndex-10)], frequency2[min(maximumIndex+10, len(frequency2))])
peak2 = analyse.peakfinder_schwerpunkt(frequency2, amplitude2)
plt.axvline(peak2)
plt.show()
