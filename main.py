cat_attributes = {
    "intelligence": 10,
    "energy": 100,
    "weight": 50,
}

print("Welcome to my cat game!")

name = input("Enter name: ")
colour = input("What colour do you want your cat to be? ")

play = True
while play == True:
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Feed your cat 4. Put your cat to sleep 5. Show stats  ")

    if option == '1':
        energy = cat_attributes["energy"]
        if energy > 30:
            cat_attributes["energy"] = energy - 10
        else: 
            print("Your cat's energy is too low to play. ")
    elif option == '2':
        energy = cat_attributes["energy"]
        if energy > 50:
            cat_attributes["energy"] = energy - 10
            intelligence = cat_attributes["intelligence"]
            cat_attributes["intelligence"] = intelligence + 10
        else:
            print("Your cat's energy is too low to train")
    elif option == '3':
        energy = cat_attributes["energy"]
        cat_attributes["energy"] = energy + 10
        weight = cat_attributes["weight"]
        cat_attributes["weight"] = weight + 2
        pass
    elif option == '4':
        cat_attributes["energy"] = 100
        pass
    elif option == '5':
        print(cat_attributes)
        pass


    if cat_attributes['energy'] < 0:
        print("Your cat's energy is low, feed it or put it to sleep")
        pass
    elif cat_attributes["intelligence"] < 0:
        print("You should train your cat")
    elif cat_attributes["weight"] < 10: 
        print("Your cat is getting small, feed it")    