def my_tuple():
    _tuple = ('Hot Dogs', 15, 193.4, 'Car Wash', True)
    print(_tuple)
    print(' ')
    for x in _tuple:
        print(x)
    print(' ')
    print(len(_tuple), ' items in tuple')
    print('Type is ', type(_tuple))
    return

def main():
    my_tuple()

main()
