cover = input("What type of cover? ")

if cover == "soft":
    answer = input("Is it perfect-bound? ")

    if answer == "yes":
        print("Soft cover books are popular!")
    else:
        print("Soft covers are great for short books!")

elif cover == "hard":
    print("Hard cover books are more expensive!")