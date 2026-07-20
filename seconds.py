str_seconds = input ("Please type the number of seconds: \n")
int_seconds= int(str_seconds)
hours = int_seconds // 3600
minutes = int_seconds % 3600 // 60
seconds = int_seconds % 60
print ("The Course is: " + str(hours) + "hours and " + str(minutes) + "minutes and " +
str(seconds) + "seconds long")