name = input("Name of the new student? ")

match name:
    case "Harry" | "Hermione" | "Ron" :
        print("Gryffindor")
    case "Draco" | "Crab" | "Goyal":
        print("Slytarin")
    case _ :
        print("Who?")