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
		
restaurant = Restaurant("massa's", "italian") 

restaurant.describe_restaurant()
restaurant.open_restaurant() 
restaurant.customers_served = 25
restaurant.number_served()

		
print("\n")
print ("9.2")

rest1 = Restaurant("O. B. Clarks", "Irish Pub")		
rest1.describe_restaurant()
rest1.set_number_served(32) 
rest1.number_served()

print ("\n")
rest2 = Restaurant("rib city", "BBQ")
rest2.describe_restaurant()
rest2.number_served()
rest2.increment_number_served(52)
rest2.number_served()

print ("\n")
rest3 = Restaurant("pasta house", "italian")
rest3.describe_restaurant()

print ("\n")
print ("9.6")


  
