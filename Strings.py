def strings(x):
    print(x)
    print(' ')
    
    for i in x:
        print(i)

    x = x + " Second"

    print(' ')
    print(x)

    y = x + " Third"

    print(' ')
    print(y)
    print(' ')
    print(x[2])

    return

def main():
    strings('First')


main()
