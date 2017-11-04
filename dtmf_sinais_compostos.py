'''
Created on 29 de out de 2017
Processamento digital de sinais 
@author: Edilson Tarcio e Rodrigo Lourenço
'''
import matplotlib.pyplot as plt
import numpy as np
import pyaudio

duracao = 1.5  # em segundos
f1 = 770.0
f2 = 1477.0  # 9
volume = 0.5  # intervalo [0.0, 1.0]

Fs = 44100  # frequencia de amostragem - DEVE SER INTEIRO
Ts = 1.0 / Fs  # intervalo de amostragem

t = np.arange(start=0, stop=duracao, step=Ts)  # vetor do tempo

y1 = np.sin(2 * np.pi * f1 * t)
y2 = np.sin(2 * np.pi * f2 * t)

y = y1 + y2

#geracao do bit

samples = y.astype(np.float32)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=Fs,
                output=True)
stream.write(volume * samples)
stream.stop_stream()
stream.close()
p.terminate()

n = len(y)  # tamanho do signal
k = np.arange(n)
T = n / Fs
frq = k / T  # dois lados do range de frequencia
frq = frq[np.arange(int(n / 2))]  # um lado do range de frequencia

# computando a Transformada de fourier e normalizando
Y = np.fft.fft(y) / n
e = range(int(n / 2))
Y = Y[e]

a = np.argsort(abs(Y))

# Arredonda os elementos da matriz para o número inteiro mais próximo
max = np.rint(frq[a[-1]])
min = np.rint(frq[a[-2]])

if max < min:
    aux = min
    min = max
    max = aux

if max == 1209.0:
    if min == 697.0:
        print("1")
    elif min == 770.0:
        print("4")
    elif min == 852.0:
        print("7")
    elif min == 941.0:
        print("*")
elif max == 1336.0:
    if min == 697.0:
        print("2")
    elif min == 770.0:
        print("5")
    elif min == 852.0:
        print("8")
    elif min == 941.0:
        print("0")
elif max == 1477.0:
    if min == 697.0:
        print("3")
    elif min == 770.0:
        print("6")
    elif min == 852.0:
        print("9")
    elif min == 941.0:
        print("#")

# plotando
fig, ax = plt.subplots(2, 1)

ax[0].plot(t[:1000], y[:1000])
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('y')

ax[1].plot(frq[:2500], abs(Y[:2500]), 'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
plt.show()