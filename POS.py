# Funksie om 'n nuwe item by die POS toe te voeg
def add_item(items):
    name = input("Voer die produknaam in: ")
    price = float(input("Voer die produkprys in: "))
    items.append((name, price))
    print(f"{name} suksesvol by die POS gestoor.")

# Funksie om 'n item van die POS te verwyder
def remove_item(items):
    if not items:
        print("Die POS is leeg. Daar is niks om te verwyder nie.")
        return
    print("Beskikbare produkte:")
    for i, (name, _) in enumerate(items):
        print(f"{i+1}. {name}")
    choice = input("Kies die nommer van die produk wat jy wil verwyder: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(items):
            removed_item = items.pop(choice - 1)
            print(f"{removed_item[0]} is suksesvol van die POS verwyder.")
        else:
            print("Ongeldige keuse. Probeer weer.")
    except ValueError:
        print("Ongeldige invoer. Voer asseblief 'n nommer in.")

# Funksie om die POS te vertoon en die totale prys te bereken
def display_pos(items):
    if not items:
        print("Die POS is leeg.")
        return
    print("Produkte by die POS:")
    total = 0
    for name, price in items:
        print(f"{name:<10} R{price:.2f}")
        total += price
    print("------------------")
    print(f"Totaal     R{total:.2f}")

# Hoofprogram
def main():
    items = []  # Lys om produkte in die POS te stoor
    while True:
        print("\nKies '1' om 'n nuwe item by die POS toe te voeg.")
        print("Kies '2' om 'n item van die POS te verwyder.")
        print("Kies '3' om die POS te vertoon en die totale prys te bereken.")
        print("Kies '4' om die program te verlaat.")
        choice = input("Kies 'n opsie: ")

        if choice == '1':
            add_item(items)
        elif choice == '2':
            remove_item(items)
        elif choice == '3':
            display_pos(items)
        elif choice == '4':
            print("Dankie vir die gebruik van die POS stelsel. Totsiens!")
            break
        else:
            print("Ongeldige keuse. Probeer weer.")

if __name__ == "__main__":
    main()