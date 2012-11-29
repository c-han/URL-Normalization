import sys
from url import URL

def readfile(f):
	result = []
	line = f.readline()
	while len(line) > 0:
		if len(line) == 1: # skip blank line
			continue
		else:
			result.append(line[:len(line) - 1])
		line = f.readline()
	return result

def main():
	# system prompt
	if len(sys.argv) is not 2:
		print 'use: python main.py <input-file>\n'
		exit(1)

	# read input file
	f = open(sys.argv[1])
	lines = readfile(f)
	
	# create URL objects
	urls = [URL(x) for x in lines]
	
	# count occurrences of original and canonical URLS
	dic_source = {}
	dic_canonical = {}
	
	for url in urls:
		if url.getURL() in dic_source:
			dic_source[url.getURL()] = dic_source[url.getURL()] + 1
		else:
			dic_source[url.getURL()] = 1
		if url.getNormalized() in dic_canonical:
			dic_canonical[url.getNormalized()] = dic_canonical[url.getNormalized()] + 1
		else:
			dic_canonical[url.getNormalized()] = 1

	# print properties of each URL read
	for url in urls:
		print "Source: " + url.getURL()
		
		if url.isValid():
			print "Valid: True"
		else:
			print "Valid: False"
			
		print "Canonical: " + url.getNormalized()
		
		if dic_source[url.getURL()] == 1:
			print "Source unique: True"
		else:
			print "Source unique: False"
			
		if dic_canonical[url.getNormalized()] == 1:
			print "Canonicalized URL unique: True\n"
		else:
			print "Canonicalized URL unique: False\n"
		
if __name__ == "__main__":
	main()