def _slice(x):
    y = slice(5)
    z = slice(0, -1, 2)
    print(x[y])
    print(x[z])

    return

def main():
    _slice('This will be sliced')

    return

main()
