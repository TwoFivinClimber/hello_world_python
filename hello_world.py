
animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan"]

for animal in animals:
    if len(animal) >= 5:
      print(animal)  


user_greeting = input("What greeting would you like? Southern, Eastern, Western").lower()

if user_greeting == "southern":
  print("Howdy y\'all")
elif user_greeting == "eastern":
  print("Hey, How ya doin\'")
elif user_greeting == "western":
  print("Chea, what up braaaaah")
else:
  print("Howdy y\'all from the South")
  
