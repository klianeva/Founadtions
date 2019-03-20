
### Challenge: How many drinks do you need to buy to throw a great party? 
# you will have a list of your friends, and their favorite drink. 
# you will also know how many drinks of a certain type are drunk per hour


#list of your friends and their favorite drink
favorite_drinks = {'Adam':'Gin and Tonic','Angela':'Mate Vodka','Sven':'Whiskey','Alexandra':'Whiskey',
                    'Michael':'White Wine','Ariana':'Gin and Tonic','Thomas':'beer','Eduardo':'White Wine',
                    'Leanne':'Red Wine', 'Karla':'Whiskey', 'Taylor': 'Mate Vodka','Jonathan':'Water'}


#types of drinks people drink, with lists of examples
cocktails = ['Gin and Tonic', 'Mate Vodka', 'Rum and Coke']

wines = ['Red Wine', 'White Wine']

liquors = ['whiskey', 'gin', 'vodka']

nonalcoholic = ['tea', 'water', 'orange juice']

beer = ["beer"]
# number of drinks per hour people drink, depeneding on the type. 
number_of_drinks_per_hour_per_type = {'cocktails':1, 'beers':3,'wines':2,'liquors':2,'nonalcoholic':3}


# The party is 6hout- how many drinks do I need to buy?
liquors_capital = []
for liquor in liquors:
    liquors_capital.append(liquor.title())

nonalcoholic_capital = []
for nonalcoholics in nonalcoholic:
    nonalcoholic_capital.append(nonalcoholics.title())
c = 0
b = 0
w = 0
l = 0
n = 0
hours = 6
for name, drink in favorite_drinks.items():
	if drink in cocktails:
		c+=1
	if drink in beer:
		b+=3
	if drink in wines:
		w+=2
	if drink in liquors_capital:
		l+=2
	if drink in nonalcoholic_capital:
		n+=3
c*=6
b*=6
w*=6
l*=6
n*=6
print ("You need to buy for the party: {} cocktails, {} beers, {} wines, {} liquors, {} nonalcoholoc drinks!".format(c,b,w,l,n))

print ("You need to buy for the party: {} cocktails, {} beers, {} wines, {} liquors, {} nonalcoholoc drinks!".format(c,b,w,l,n))
