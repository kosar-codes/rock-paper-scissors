import random
option=["rock","paper","scissors"]

print("---hiii.let`s play rock,paper,scissors---")

while True:
    user_choise=input("enter rock,paper,scissors:").lower()
    computer_choise=random.choice(option)
    print("computer chose:",computer_choise)
    
    if computer_choise==user_choise:
        print("it`s a tie!!!")
        
    elif computer_choise=="scissors" and user_choise=="rock":
        print("you wiiin!!!")
    
    elif computer_choise=="rock" and user_choise=="paper":
        print("you wiin!!!")
        
    elif computer_choise=="paper" and user_choise=="scissors":
        print("you wiiin!!!")
        
    else:
        print("computer winnnnn")
    
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again != "Y":
       print("Thanks for playing! byeeeee.")
       break