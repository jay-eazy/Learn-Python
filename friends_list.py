# len function = length, which tells the length of a list
# for function needs an iterable object such as a list, [0,1,2], and then it gives value to it
    # ex: for _ in [1,2,3] has 3 values
# range function essentially created a list
    #ex: range(3)= [0,1,2]
my_friends= ["chuma","gab","jorge","caiden"]
for friend in range(len(my_friends)):
    print(friend+1, my_friends[friend])
