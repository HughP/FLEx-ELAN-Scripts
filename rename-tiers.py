# -*- coding: utf-8 -*-
# This tells python that parts of the script are utf-8

"""
rename-tiers.py
This is just a series of regex replacements, renaming all tiers in an ELAN file using a single command. It is designed to replace the default post-Flex tier names, which are awkward.
... Seems to need something more to rename the linguistic types???
"""

import sys, re, os, shutil, time, datetime

ts = time.time()
datestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_')

def usage():
	print """
#################################################
# USAGE INSTRUCTIONS: rename-tiers.py
#################################################

You must provide the input file name as a command line argument.

"""

def main():
	
	if not len(sys.argv)>1:
		print "No target file specified"
		# Get set of all input files; for the moment just everything in current directory
		#inputfiles = get_inputs('.')
		sys.exit()
	else:
		inputfiles = [sys.argv[1]]

	# Also give the same treatment to the associated pfsx (formatting) file
	pfsxFile = re.sub('.eaf', '.pfsx', inputfiles[0])
	inputfiles.append(pfsxFile)

	for infile in inputfiles:
		print "doing file... "+infile

		inputFile = open(infile, 'r')
		lines = inputFile.readlines()

		#now we can just overwrite the original
		outFileName = infile + '.edit.xml'
		outputFile = open(outFileName, 'w')
		
		for line in lines:
			newLine = line
			newLine = re.sub('phrase-txt-mwf', 'phrase', newLine)
			newLine = re.sub('phrase-gls-en', 'trans', newLine)
			newLine = re.sub('phrase-comment-en', 'comment', newLine)
			newLine = re.sub('word-txt-mwf', 'word', newLine)
			newLine = re.sub('morph-txt-mwf', 'morph', newLine)
			newLine = re.sub('morph-cf-mwf', 'citeMorph', newLine)
			newLine = re.sub('morph-gls-en', 'gls', newLine)
			newLine = re.sub('morph-msa-en', 'partSpeech', newLine)
			#newLine = re.sub('', '', newLine)
			outputFile.write(newLine)


if __name__ == "__main__":
    main()