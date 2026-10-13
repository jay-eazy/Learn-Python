name = input("what is your name?")

match name:
    case"Harry" | "Hermione" | "Ron":
        print("Gryfidor")
    case("draco:"):
        print("snake")
    case(_):
        print("cat")