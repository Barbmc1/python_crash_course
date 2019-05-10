class Restaurant():
	"""A simple class to model a restaurant"""
	def __init__(self, name, cuisine_type):
		"""Initialize the name & type of food"""
		self.name = name
		self.cuisine_type = cuisine_type
		self.customers_served = 0
		
	def describe_restaurant(self):
		"""Provides the name of the restaurant & the type of food served"""
		print (self.name.title() + " " + self.cuisine_type.title())
		
	def open_restaurant(self):
		"""Indicates that the restaurant is open"""
		print ("This restaurant is open!")
		
	def number_served(self):
		"""This tells the number of customers served at the restaurant"""
		print ("The number of customers served here is " + str(self.customers_served))
		
	def set_number_served(self, ate):
		"""This method will allow the number of customers to be changed"""
		self.customers_served = ate
		
	def increment_number_served(self, people):
		"""This method will incriment the number of customers served"""
		self.customers_served += people
		
		
class IceCreamStand(Restaurant):
	"""This class inheriates from the Restaurant Class and adds code to handle flavors."""
	def __init__(self, name, cuisine_type):
		"""Initializes attributes of the parent class."""
		super().__init__(name, cusine_type)	
		self.flavors ['vanilla', 'chockolate',	'strawberry', 'orange', 'bubble gum']
		
		def get_flavors(self):
			print(flavors)
			
	cool_scoops = IceCreamStand("cool scoops", "ice-cream")
	cool_scoops.describe_restaurant
	cool_scoops.get_flavors
