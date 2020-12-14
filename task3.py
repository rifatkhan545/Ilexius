def likes(people):
    if len(people) == 0:
        print('no one likes this')
    elif len(people) == 1:
        print("{} likes this".format(people[0]))

    elif len(people) == 2:
        print("{} and {} likes this".format(people[0], people[1]))

    elif len(people) == 3:
        print("{}, {} and {} likes this".format(people[0], people[1], people[2]))
    else:
        print("{}, {} ".format(people[0], people[1]) + "and " + str(len(people) - 2) + " likes this")


likes([])
likes(["Peter"])
likes(["Jacob", "Alex"])
likes(["Max", "John", "Mark"])
likes(["Alex", "Jacob", "Mark", "Max"])
likes(["Alex", "Jacob", "Mark", "Max", "Rashed"])
