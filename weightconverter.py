# a simple weight converter with condition as part of my python Basics learning

# help as find our weight in any other planet in our solar system



print('=====================WEIGHT CONVERTER======================')

earth_weight = float(input('enter your earth weight in Kg'))
relative_gravity = 0
planet_num = int(input('enter ur planet num'))
planet = str()

if planet_num == 1 :
    planet = "Mercury"
    relative_gravity = relative_gravity+ 0.38
elif planet_num == 2 :
    planet = "Venus"
    relative_gravity = relative_gravity + 0.91
elif planet_num == 3 :
    planet = "Mars"
    relative_gravity = relative_gravity + 0.38
elif planet_num == 4 :
    planet = "Jupiter"
    relative_gravity = relative_gravity + 2.53
elif planet_num == 5 :
    planet = "Saturn"
    relative_gravity = relative_gravity + 1.07
elif planet_num == 6 :
    planet = "Uranus"
    relative_gravity = relative_gravity + 0.89
elif planet_num == 7 :
    planet = "Neptune"
    relative_gravity = relative_gravity + 1.14
else :
    print(' invalid input ')    


  

des_weight = float(earth_weight * relative_gravity)   # destination weight=Earth weight × relative gravity

print(f'Your weight in {planet} is  {des_weight} Kg') 

print("THANK YOU ")






