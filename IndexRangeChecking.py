def checkIndex(x, y):
    print(0 <= y < len(x))
    return

def main():
    myList = [1, 2, 3, 4, 5]
    checkIndex(myList, 0)
    checkIndex(myList, 1)
    checkIndex(myList, 2)
    checkIndex(myList, 3)
    checkIndex(myList, 4)
    checkIndex(myList, 5)

    return

main()
