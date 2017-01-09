
meal_cost = input()
tip_percent = input()
tax_percent = input()

def calculate_cost(meal_cost, tip_percent, tax_percent):
	tip = meal_cost * tip_percent / 100
	tax = meal_cost * tax_percent / 100
	total_cost = meal_cost + tip + tax
	total_cost = round(total_cost)
	total_cost = int(total_cost)
	print "The total meal cost is {} dollars.".format(total_cost)


calculate_cost(meal_cost, tip_percent, tax_percent)
