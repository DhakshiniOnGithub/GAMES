films = {
    "Finding Dory":[3,5],
    "Raya and the last Dragon":[8,5],
    "Frozen":[5,5],
    "Moana":[5,9],
    }

while True:
    choice = input("What film do you want to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
        if age >=films[choice][0]:

            if films[choice][1]>0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry we are sold out")
        else:
            print("You're to young to watch the movie")
    else:
        print("We don't have that fillm...")
