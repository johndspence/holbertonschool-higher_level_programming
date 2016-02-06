print "Welcome to the taxes and tip calculator!"
print "What is the price before tax?",
price = raw_input()
print "What are the taxes (in %)",
taxes = raw_input()
print "What do you want to tip (in %)",
tip = raw_input()
pay = int(price) * ( 1+ float(taxes) / 100) * (1 + float(tip) / 100 )
print "The price you need to pay is: $", "%.6f" % pay