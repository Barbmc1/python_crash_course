import csv

from matplotlib import pyplot as plt

filename = 'Dollhouses.csv'

"""This will open and read the file, collecting all wholesale $ reatial prices.
A chart showing bith prices for each item will be plotted, and the markup for 
the products will be shaded in blue."""
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	products, retails, wholesales = [], [], []
	for row in reader:
		products.append(row[0])
		retail = float(row[3])
		retails.append(retail)
		
		wholesale = float(row[2])
		wholesales.append(wholesale)
	
#Plot data
fig = plt.figure(dpi=128, figsize=(30, 6))
plt.plot(products, retails, c='green', alpha=0.5)
plt.plot(products, wholesales, c='blue', alpha=0.5)
plt.fill_between(products, retails, wholesales, facecolor='blue', alpha=0.1)

#Format plot
plt.title("Wholesale Vs. Retail Pricing", fontsize=24)
plt.xlabel('Products ', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("US Dollars", fontsize=16)
plt.tick_params(axis='x', which='major', labelsize=7)
plt.tick_params(axis='y', which='major', labelsize=16)

plt.show()

	
