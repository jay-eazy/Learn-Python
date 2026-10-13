def main():
     difficulty= input("Do you like easy or difficult games?")
     if difficulty == "easy":
         game = "animal crossing"
         reccomend(game)
     elif difficulty == "difficult":
         game = "dark souls"
         reccomend(game)

def reccomend(game):
    print("you might like", game)
main()