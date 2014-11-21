#!/usr/bin/env python

import template as TMP
import os
import random as rnd

rnd.seed(1)
voices = []

noteNames = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]
noteLength = ["1.", "1", "2.", "2", "4.", "4", "8.", "8", "16", "32"]
octaves = [",,,", ",,", ",","", "'", "''", "'''"]
instruments = ["acoustic grand", "acoustic grand", "acoustic grand", "acoustic grand"]


for i in range(4):
	notesList = []
	for k in range(100):
		rndNote = rnd.randint(0,len(noteNames)-1)
		rndLen = rnd.randint(0,len(noteLength)-1)
		rndOct = rnd.randint(0,len(octaves)-1)
		notesList.append(" " + noteNames[rndNote] + octaves[rndOct] + noteLength[rndLen])

	voices.append(TMP.OneVoice\
		.replace("__@NOTES__", 	' '.join(notesList) )
		.replace("__@OCTAVE__", "'")
		.replace("__@INSTRUMENT__",instruments[i]))


# output midi
concat_voices = ' '.join(voices)
output = TMP.ScoreTemplate.replace("__@VOICES__", concat_voices)

f = open("test.ly","w")
f.write(output)
f.close()

os.system("lilypond test.ly")

# synthesize wav
os.system("timidity --output-24bit -A120 test.midi -Ow -o test.wav")


