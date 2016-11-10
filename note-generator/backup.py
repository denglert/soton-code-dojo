import math
import struct
import pyaudio
import random

ampl = math.exp(5)

def play_tone(frequency, amplitude, duration, fs, stream):
    N = int(fs / frequency)
    T = int(frequency * duration)  # repeat for T cycles
    dt = 1.0 / fs
    # 1 cycle
    tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
            for n in xrange(N))
    # todo: get the format from the stream; this assumes Float32
    data = ''.join(struct.pack('f', samp) for samp in tone)
    for n in xrange(T):
        stream.write(data)

def just_play(freq):
		  play_tone(freq, ampl, 0.1, fs, stream)

#########################

fs = 48000
#fs = 500
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=fs,
    output=True)

# play the C major scale
scale = [130.8, 146.8, 164.8, 174.6, 195.0, 220.0, 246.9, 261.6]

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()




getch = _Getch()
keys = ['a','s','d','f','g','h','j','k']
scale = [130.8, 146.8, 164.8, 174.6, 195.0, 220.0, 246.9, 261.6]

frange = 0
tonedict = dict(zip(keys,scale[frange:frange+len(keys)-1]))

length = 0.3

while True:
	a = getch()
	print(a)

	if a in tonedict:
  		play_tone(tonedict[a], ampl, length, fs, stream)

	if a == b'\x1b':
	    break



