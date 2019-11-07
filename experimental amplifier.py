quit = False

while not quit:
    sourceStr = input()
    if sourceStr == 'quit':
        quit = True
    else:
        sourceStr2 = set(sourceStr)
        source = set()

        if len(sourceStr) != 0:
            for _ in sourceStr:
                if _ == '0':
                    print('Please enter a number between 1-9 and dont use empty spaces!')
                    break
                elif _.isalpha():
                    print('Please enter a number between 1-9 and dont use empty spaces!')
                    break
                else:
                    quit = True
        else:
            print('Please enter a number between 1-9 and dont use empty spaces!')

try:
    for x in sourceStr:
        source.add(int(x))

    amplified = sum(source)
    rest = amplified
    base = len(source)
    target = ''
    if base == 1:
        base = 10
        

    for _ in range(base):
        target = str(rest % base) + target
        if rest // base == 0:
            break
        else:
            rest = rest // base

    print(amplified, base, target)
except:
    print('Something went wrong, please try again...')