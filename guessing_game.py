import random
minNum = 1
maxNum = 9
correctNum = random.randint(minNum, maxNum)
while True:
    try:
        cmd = input(f'Enter a number between {minNum} and {maxNum} inclusive (or "exit")')
        if cmd == 'exit':
            break
        
        guess = int(cmd)
        if guess < minNum or guess > maxNum:
            print('Out of range')
        elif guess == correctNum:
            print(f'Yes - the correct number is {correctNum}')
            break        
        elif guess < correctNum:
            print('Higher')
        else:
            print('Lower')
    except:
        print('Invalid entry')