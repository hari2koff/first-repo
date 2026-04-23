#cyclone
height = int(input("Height: ")) # in cm
credits = int(input("Credit: "))

if height > 137 and credits > 10:  # for both having (and) true
  print("Enjoy the ride!")
elif height < 137 and credits > 10:
  print("height does not meet the requiment") # for either condition(or) and follwoing for either condition with other if
elif  height > 137 and credits < 10:
  print("not enough credit")  
else :   #for both not true
  print(" you don't meet either of the requirment")  
    

