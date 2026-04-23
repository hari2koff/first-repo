#sorting hat
print("=================Sorting Hat=====================")



Gryffindor = 0
Ravenclaw  = 0
Hufflepuff = 0
Slytherin  = 0

#  question 1 

print("Q1) Do you like Dawn or Dusk? ")
print("1) Dawn ")
print("2) Dusk ")

ans = int(input("Enter your answer "))

if ans == 1 :
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif ans == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else :
    print ("wrong input ")    

# question 2 

print("Q2) When I’m dead, I want people to remember me as: ")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

ans_1 = int(input("Enter your answer"))

if ans_1 == 1:
    Hufflepuff = Hufflepuff +2
elif ans_1 == 2:
    Slytherin = Slytherin + 2
elif ans_1 == 3 :
    Ravenclaw = Ravenclaw + 2
elif ans_1 == 4 :
    Gryffindor = Gryffindor + 2
else :
    print("Invalid output ")

# question 3 

print("Q3) Which kind of instrument most pleases your ear? ")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

ans_2 = int(input("Enter your answer "))

if ans_2 == 1 :
    Slytherin = Slytherin + 4
elif ans_2 == 2 :
    Hufflepuff = Hufflepuff + 4
elif ans_2 == 3 :
    Ravenclaw = Ravenclaw + 4
elif ans_2 == 4 :
    Gryffindor = Gryffindor + 4    
else :
    print("Invalid input ")    

print(Gryffindor)
print(Ravenclaw)
print(Slytherin)
print(Hufflepuff)






        


