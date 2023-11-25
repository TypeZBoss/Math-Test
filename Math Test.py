print("Welcome to the math quiz choose your level")
print("Easy")
print("Normal")
print("Hard")

Level = input('')
Right = 0

if Level == "Easy":
    Answer = input("3+5 ")
    if Answer == "8":
        print("Correct!")
        Right = 1
    else:
        print("Wrong!")

    Answer = input("5+5 ")
    if Answer == "10":
        print("Correct!")
        Right = 2
    else:
        print("Wrong!")

    Answer = input("9-4 ")
    if Answer == "5":
        print("Correct!")
        Right = 3
    
    else:
        print("Wrong!")
    print("You got " + str(Right ) + "/3" +" questions right!")

if Level == "Normal":
    Answer = input("17-8 ")
    if Answer == "9":
        print("Correct!")
        Right = 1
    else:
        print("Wrong!")

    Answer = input("21-7 ")
    if Answer == "14":
        print("Correct!")
        Right = 2
    else:
        print("Wrong!")

    Answer = input("8*4 ")
    if Answer == "32":
        print("Correct!")
        Right = 3
    
    else:
        print("Wrong!")
    print("You got " + str(Right ) + "/3" +" questions right!")

if Level == "Hard":
    Answer = input("6*9 ")
    if Answer == "54":
        print("Correct!")
        Right = 1
    else:
        print("Wrong!")

    Answer = input("3*9 ")
    if Answer == "27":
        print("Correct!")
        Right = 2
    else:
        print("Wrong!")

    Answer = input("49/7 ")
    if Answer == "7":
        print("Correct!")
        Right = 3
    
    else:
        print("Wrong!")
    print("You got " + str(Right ) + "/3" +" questions right!")

            
            
    