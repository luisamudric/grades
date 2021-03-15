

while True:
    grade = input('Please enter your percentage mark (type quit to exit): ')
    if grade == 'quit':
        break
    try:
        grade = int(grade)
    except:
        print('The percentage should be a number between 1 - 100')
    else:
        if grade >= 85 and grade <=100:
            print('You got an A')
        elif grade >= 70 and grade < 85:
            print('You got a B')
        elif grade >= 55 and grade < 70:
            print('You got a C')
        elif grade >= 40 and grade < 55:
            print('You got a D')
        elif grade <= 54 and grade >= 0:
            print('You got an F')
        else:
            print('Please enter a valid grade (1 - 100)')
