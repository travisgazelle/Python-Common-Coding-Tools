class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

def main():
    car1 = Car('Honda', 'Civic', 2021)
    car2 = Car('Subaru', 'Forester', 2017)

    print('Car one is a', car1.year, car1.make, car1.model)
    print('Car two is a', car2.year, car2.make, car2.model)

    return

main()
