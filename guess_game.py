import random #to generate random numbers

random_number= random.randint(1,101) #gentrate a random number between 1 and 100

count=0
guess=-99
while(guess!=random_number):
    #Get the user guess
    guess =  int(input("Enter your guess between 1 and 100:"))

    if guess < random_number:
        print("higher")
    elif guess > random_number:
        print("lower")
    else:
        print("you gussed it!")
        break
    count=count+1
#end of while loop

print("You took " +str(count)+ " turns to guess the number correctly.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
