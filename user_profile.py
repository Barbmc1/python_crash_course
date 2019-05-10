print ("9.3")

class User():
	"""This is collects information on a user."""
	def __init__(self, first_name, last_name, password, year_born):
		"""Initialize attributes for class user."""
		self.first_name = first_name
		self.last_name = last_name
		self.password = password
		self.year_born = year_born
		self.login_attempts = 0
		
	def describe_user(self):
		"""Neatly print out the user profile information"""
		print (self.first_name.title() + " "  + self.last_name.title() + " " + str(self.password)  + " " + str(self.year_born))
		
	def great_user(self):
		print ("hello " + self.first_name.title() + " " + self.last_name.title() + "!")
		
	def increment_login_attempts(self, attempt):
		"""This will count the number of times a user attempts to log in"""
		self.login_attempts += attempt
		print (str(self.login_attempts))
		
	def reset_login_attempts(self):
		"""Resets the login count to zero."""
		self.login_attempts = 0
		


user1 = User("barbara", "mcghee", "PaSsWoRd", "1972")
user1.describe_user()
user1.great_user()

print("\n")
user2 = User("mary", "smith", "GreatMe", "1964")
user2.describe_user()
user2.great_user()

print("\n")
user3 = User("TOM", "KELLY", "GoCards1", "1982")
user3.describe_user()
user3.great_user()


print ("\n")
print ("9.5")
user4 = User("Mike", "Thompson", "May2019!", "2000")
print (user4.login_attempts)
user4.increment_login_attempts(1)
user4.reset_login_attempts()
print (user4.login_attempts)
