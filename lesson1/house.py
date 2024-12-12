name = input("whats your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("slytherin")
    else:
        print ("who?")

