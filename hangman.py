import random
with open("hangman.txt","r") as f:
    word=f.readlines()
tu_can_doan=random.choice(word)[:-1]
tu_doan_duoc=""
dem=5
check=0
kt=0
print("Here is your puzzle")
print("_"*len(tu_can_doan))
while dem >0:
    doan=str(input("Enter your guess: "))
    if doan in tu_can_doan:
        print(f'Congratulations, you guessed a letter {doan} in the puzzle!')
    else:
        dem-=1
        print(f"Sorry,letter {doan} is NOT in the puzzle, you have {dem} chances left")
        
    tu_doan_duoc=tu_doan_duoc+doan

    for letter in tu_can_doan:
        if letter in tu_doan_duoc:
            print(f'{letter}',end='')
        elif letter not in tu_doan_duoc:
            print("_",end='')
    print("")
    for i in range(len(tu_can_doan)):
        if tu_can_doan[i] ==doan :
            check+=1
    # for chu in tu_doan_duoc:
    #     if chu==doan:
    #         kt+=1
    # if kt>1:
    #     dem-=1
    #     print("lap lai")
    if dem==0:
        print("Sorry, you have made 5 incorrect guesses, you lose")
        print(f'The correct word is {tu_can_doan}')
        exit()
    if check==len(tu_can_doan):
        print("You win the game")
        exit()
    

        

