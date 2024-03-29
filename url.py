from urlnorm import norm

""" URL CLASS """
class URL:
	def __init__(self, address):
		self.url = address
		self.normalized = norm(address)

	def isValid(self):
		return self.url == self.normalized

	def getURL(self):
		return self.url
	
	def getNormalized(self):
		return self.normalized

	""" URL Comparator using normalized strings """
	def __lt__(self, other):
		if self.isValid() != other.isValid():
			return self.isValid > other.isValid()
		else:
			return self.normalized < other.normalized

	def __le__(self, other):
		if self.isValid() != other.isValid():
			return self.isValid > other.isValid()
		else:
			return self.normalized <= other.normalized

	def __gt__(self, other):
		if self.isValid() != other.isValid():
			return self.isValid < other.isValid()
		else:
			return self.normalized > other.normalized

	def __ge__(self, other):
		if self.isValid() != other.isValid():
			return self.isValid < other.isValid()
		else:
			return self.normalized >= other.normalized

	def __eq__(self, other):
		if self.isValid() != other.isValid():
			return False
		else:
			return self.normalized == other.normalized

	""" Other functions using normalized strings """
	def __len__(self):
		return len(self.normalized)

	def __getitem__(self, index):
		return self.normalized[index]
