import sys
import os.path

def getJumbleDict(filePath):
	with open(filePath) as f:
		wordlist = f.readlines()
		jumbles = {}
		for word in wordlist:
			word = word.strip().lower()
			wsorted = ''.join(sorted(word))
			if wsorted in jumbles:
				jumbles[wsorted].append(word)
			else:
				jumbles[wsorted] = [word]
		return jumbles

def allCombinations(word):
	if not word:
		return [[]]
	return [[word[0]] + x for x in allCombinations(word[1:])] + allCombinations(word[1:])

def allJumbleKeys(word):
	combinations = allCombinations(word.strip().lower())
	keys = [''.join(sorted(x)) for x in combinations]
	return set(keys)

def playWordJumble(jumbleDict):
	while True:
		word = raw_input('Please enter word for jumble (q to quit): ').strip().lower()
		if word == 'q':
			break
		if len(word) > 0:
			keys = allJumbleKeys(word)
			words = []
			[words.extend(jumbleDict[x]) for x in keys if x in jumbleDict]
			wordOrLetters = ''
			if word in words:
				wordOrLetters = 'word'
			else:
				wordOrLetters = 'letters'
			print '%i words can be made from the %s "%s"' % (len(words), wordOrLetters, word)
			print words

def main():
	filePath = 'wordlist.txt'
	if len(sys.argv) > 1:
		filePath = sys.argv[1]
	if os.path.isfile(filePath):
		jumbleDict = getJumbleDict(filePath)
		playWordJumble(jumbleDict)
	else:
		print 'Word list at %s not available.' % filePath


if __name__ == "__main__":
	main()
