class Movie():
	"""
	A class that stores information about a movie
	"""
	
	def __init__(self, title, description, poster, trailer):
		"""
		Initializes a movie object when the class is called
		"""
		self.title = title
		self.description = description
		self.poster = poster
		self.trailer = trailer