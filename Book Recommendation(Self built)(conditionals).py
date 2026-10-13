def main():
    difficulty = input("What difficulty do you like your books?")
    genre = input("What genre do you like your books?")
    if difficulty == "easy":
        if genre == "fantasy":
            recommend("Wizard of Oz")
        elif genre == "drama":
            recommend("Ruby Holler")
        else:
            print ("Sorry, I don't know your genre")
    elif difficulty == "medium":
        if genre == "fantasy":
            recommend("Harry Potter")
        elif genre == "drama":
            recommend("Becuase of Winn-Dixie")
        else:
            print ("Sorry, I don't know your genre")
    elif difficulty == "hard":
        if genre == "fantasy":
            recommend("the stormlight series")
        elif genre == "drama":
            recommend("Don Quixote")
    else:
        print ("Sorry, I don't know your difficulty")


def recommend(book):
    print(" I bet you'd like",book)
main()
