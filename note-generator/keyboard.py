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
keys_user = ['a','s','d','f','g','h','j']
keys_user2 = ['A','S','D','F','G','H','J']
keys_note = ['c','d','e','f','g','a','b']
scale = [130.8, 146.8, 164.8, 174.6, 195.0, 220.0, 246.9, 261.6]

frange = 0
tonedict_user  = dict(zip(keys_user,scale[frange:frange+len(keys_user)-1]))
tonedict_user2 = dict(zip(keys_user2,scale[frange:frange+len(keys_user2)-1]))
tonedict_note  = dict(zip(keys_note,scale[frange:frange+len(keys_note)-1]))

length = 0.5
length2 = 1.

def play_on_key():
	while True:
		a = getch()
		print(a)
	
		if a in tonedict_user:
	  		play_tone(tonedict_user[a], ampl, length, fs, stream)
	
		if a == b'\x1b':
		    break

def play_from_file():
	with open("notes2.txt") as f:
		for line in f:
			for c in line.split():
				print c
	  			play_tone(tonedict_note[c], ampl, length, fs, stream)


def main():
	#play_on_key()
	play_from_file()


if __name__ == "__main__":
	main()
