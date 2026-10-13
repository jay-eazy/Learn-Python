emoticon = (";-;")

def main():
     global emoticon
     say("is anyone here")
     emoticon= (":)")
     say("wassup")

def say(phrase):
    print(phrase + emoticon)
main()
# side effect is anything changed while running a script
# Global function allows to make you alter a global variable inside of a variable
#This is a side effect, which will affect everything down the line that relies on emoticon