from pypesq import pesq
import soundfile as sf

s, sr = sf.read('mix.wav')
m, sr = sf.read('clean.wav')

print('score: ', pesq(m, s))
