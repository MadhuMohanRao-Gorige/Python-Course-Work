#3.Take temperature input and:
#If above 30: print “It’s hot”
#If between 15 and 30: print “Pleasant”
#If below 15: print “Cold”
a=int(input("Take temperature:"))
if a>=30:
    print("It's hot")
elif a>=15 and a<=30:
    print("Pleasent")
else:
    print("Cold")
