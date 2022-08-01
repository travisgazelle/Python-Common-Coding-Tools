def checkForItem(_dict, key):
    if key in _dict:
        print(_dict[key])
    else:
        print("No results found")

    return

def main():
    carInventory = {
        "Toyota": "Tacoma",
        "Honda": "Civic",
        "Volkswagen": "Passat",
        "Audi": "A3"
        }
    checkForItem(carInventory, "Toyota")
    checkForItem(carInventory, "Audi")
    checkForItem(carInventory, "Honda")
    checkForItem(carInventory, "Volkswagen")
    checkForItem(carInventory, "Porsche")

    return

main()
