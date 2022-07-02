import random
number_of_bulls = 0
number_of_cows = 0
numberCheck = 0
playerNum = 0
cpuNum = []
correctGuess = 0

while numberCheck == 0:
    cpuNum.append(str(random.randint(1,9)))
    for i in range(3):
        cpuNum.append(str(random.randint(0,9)))   
    cpuSet = set(cpuNum)
    if len(cpuNum) == len(cpuSet):
        numberCheck = 1
print(cpuNum)
while correctGuess == 0:
    playerNum = str(input("What is your 4-digit guess? (no repeats): "))
    for i in range(4):
        if cpuNum[i] == playerNum[i]:
            number_of_bulls = number_of_bulls + 1
        if cpuNum[i] in playerNum:
            number_of_cows = number_of_cows + 1
    print("Bulls:", number_of_bulls)
    print("Cows:", number_of_cows - number_of_bulls)
    if number_of_bulls == 4:
        print("Congrats, you win!")
        correctGuess = 1