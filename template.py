#!/usr/bin/env python

ScoreTemplate = """
\\version "2.14.2"
\\score{
	\\new Staff <<
		\\tempo 4 = 40
		__@VOICES__
	>> 
	\\midi
	{
		\\context
		{
			\\Voice
			\\consists "Staff_performer"
		}
	}
}
"""


OneVoice = """
	\\new Staff
	{
		\\new Voice{
			\\set midiInstrument = #"__@INSTRUMENT__"
			__@NOTES__
		}
	}
"""



