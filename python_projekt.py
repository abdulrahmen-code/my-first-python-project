str_length = input ("Please type length: \n")
str_width = input ("Please type width: \n")
str_meter = input ("How much for 1 meter? \n")
length = float (str_length)
width = float (str_width)
meter = float (str_meter)
area = length * width 
prise = area * meter 
print ("The total area is: " + str(area))
print ("Give the guy: " + "$" + str(prise))