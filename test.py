from url import URL

def testValidity(url, expected):
	if URL(url).isValid() == expected:
		print "+ Validity PASS"
	else:
		print "- Validity FAIL"
		
def testNormalization(url, expected):
	result = URL(url).getNormalized();
	if result == expected:
		print "+ Normalization PASS"
	else:
		print "- Normalization FAIL: result was " + result

""" Tests URL validity and normalization """
def main():
	# validity test
	# 1 for valid; 0 for invalid
	testValidity("example.com", 0)
	testValidity("aaa", 0)
	testValidity(" ", 0)
	testValidity("http://example.com/", 1)
	testValidity("http://example.com/#", 1)
	testValidity("http://example.com/a#", 1)
	testValidity("http://example.com/a#bb", 1)
	testValidity("http://example.com/aa#bb#cc", 0)
	testValidity("http://g.com/", 1)
	testValidity("http://www.example.com", 0)
	testValidity("http://example.com home", 0)
	testValidity("http://example.com []", 0)
	testValidity("http://example.com ()", 0)
	testValidity("http://example.ca/", 1)
	testValidity("http://example.co.kr/", 1)
	testValidity("example.co.uk/", 0)
	testValidity("example.co.uk", 0)
	
	# normalization test
	testNormalization("HTTP://www.Example.com/", "http://www.example.com/")
	testNormalization("http://www.example.com/a%c2%b1b", "http://www.example.com/a%C2%B1b")
	testNormalization("http://www.example.com/%7Eusername/", "http://www.example.com/~username/")
	testNormalization("http://www.example.com:80/bar.html", "http://www.example.com/bar.html")
	testNormalization("http://www.example.com", "http://www.example.com/")
	testNormalization("http://www.example.com/../a/b/../c/./d.html", "http://www.example.com/a/c/d.html")
	testNormalization("http://www.example.com/foo//bar.html", "http://www.example.com/foo/bar.html")
	testNormalization("http://www.example.com/display?", "http://www.example.com/display")
	testNormalization("example.com", "http://example.com/")
	testNormalization("http://ExAmPlE.cOm", "http://example.com/")
	testNormalization("http://de.wikipedia.org/wiki/Elf (Begriffsklarung)", "http://de.wikipedia.org/wiki/Elf%20(Begriffsklarung)")
	testNormalization("ftp://example.com", "ftp://example.com/")

if __name__ == "__main__":
	main()