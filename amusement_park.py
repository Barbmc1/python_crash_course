age = 12

if age <4:
	print ("Your admission is $0.")
elif age < 18:
	print ("Your admission is $5.")
else:
	print ("Your admission is $10.")
	
print("\n")
age = 19
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
	
print ("Your admission cost is $" + str(price) + ".")


print("\n")
age = 68
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age > 65:
	price = 5
	
print ("Your admission cost is $" + str(price) + ".")
