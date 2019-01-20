#!/usr/bin/env python3

from googletrans import Translator
import sys

translator = Translator()

dest = 'hr'

if len(sys.argv) > 1:
	try:
		dest = sys.argv[2]
	except:
		pass
			
	translated = translator.translate(sys.argv[1],  dest = dest)
	print(translated.text)

