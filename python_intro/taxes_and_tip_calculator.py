# This is a brief Python program, entitled "taxes and tip calculator" by John
# Spence.  The program is designed to calculate total price to pay for a meal
# after taxes and tip are added.

print "Welcome to the taxes and tip calculator!" # Welcome message to user

print "What is the price before tax?", # Prompts user for meal price
price = raw_input() # Accepts inputted meal price in raw format

print "What are the taxes? (in %)", # Prompts user for tax rate as a %
taxes = raw_input() # Accepts inputted tax rate in raw format

print "What do you want to tip? (in %)", # Prompts user for tip as a %
tip = raw_input() # Accepts inputted tip % in raw format

pay = float(price) * ( 1+ float(taxes) / 100) * (1 + float(tip) / 100 )
# Calculates variable "pay" (amount to be paid) by multiplying:
# integer form of price * float form of taxes * float form tip

print "The price you need to pay is: $%.6f." % pay
# Output message