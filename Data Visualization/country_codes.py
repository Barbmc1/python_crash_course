from pygal.maps.world import COUNTRIES



def get_country_code(country_name):
	"""Returm the 2-digit country code for the gioven country."""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
		#If the country wasn't found, return None.
		return None

print(get_country_code('United Arab Emirates'))
	
print(get_country_code('Andorra'))

print(get_country_code('Arab World'))
