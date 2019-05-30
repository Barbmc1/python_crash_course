class Car():
	"""A simple attempt to represent a car."""
	
	def __inti__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formated descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		"""Print a statement showing the car's milage."""
		print ("This cas has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, milage):
		"""Set the odometer reading to a given value.
		Reject the change if it attempts to roll the odometer back."""
		if milage >= self.odometer_reading:
			self.odometer_reading = milage
		else:
			print ("You can't roll back an odometer!")
			
	def incriment_odometer(self, miles):
		"""Add given amount to the odometer reading."""
		self.odometer_reading += miles
