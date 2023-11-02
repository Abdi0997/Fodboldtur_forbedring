import pickle

filename = 'betalinger.pk'
fodboldtur = {}

def afslut():
    with open(filename, 'wb') as outfile:
        pickle.dump(fodboldtur, outfile)
    print("Programmet er afsluttet!")

def printliste():
    for spiller, betaling in fodboldtur.items():
        mangler = max(4500 - betaling, 0)
        print(f"{spiller}: Har betalt {betaling} DKK, Mangler at betale: {mangler} DKK")

def registrer_betaling():
    input_str = input("Indtast betaling (syntax: {spiller} {beløb}): ")
    try:
        beløb_index = next((i for i, c in enumerate(input_str) if c.isdigit()), None)
        if beløb_index is None:
            raise ValueError("Ugyldig input. Mangler beløb.")
        spiller = input_str[:beløb_index].strip().title()
        beløb = float(input_str[beløb_index:])
    except ValueError:
        print("Forkert inputformat. Brug syntaxen: {spiller} {beløb}")
        return
    fodboldtur[spiller] = fodboldtur.get(spiller, 0) + beløb
    print(f"{spiller} har betalt {beløb} DKK")
    print(f"{spiller} mangler nu {4500 - beløb} DKK")
    gem_data(fodboldtur)

def gem_data(data):
    with open(filename, 'wb') as outfile:
        pickle.dump(data, outfile)

def tre_mest_manglende():
    manglende_liste = []
    for spiller, betaling in fodboldtur.items():
        mangler = max(4500 - betaling, 0)
        manglende_liste.append((spiller, mangler))
    manglende_liste.sort(key=lambda x: x[1], reverse=True)
    print("De tre mest manglende medlemmer:")
    for index, (spiller, mangler) in enumerate(manglende_liste[:3], start=1):
        print(f"{index}. {spiller}: Mangler at betale {mangler} DKK")

def menu():
    while True:
        print("MENU")
        print("1: Se liste over betalinger")
        print("2: Registrer betaling")
        print("3: Se de tre der mangler mest")
        print("4: Afslut program")
        valg = input("Indtast dit valg: ")
        if valg == '1':
            printliste()
        elif valg == '2':
            registrer_betaling()
        elif valg == '3':
            tre_mest_manglende()
        elif valg == '4':
            afslut()
            break
        else:
            print("Ugyldigt valg. Prøv igen.")

try:
    with open(filename, 'rb') as infile:
        fodboldtur = pickle.load(infile)
except FileNotFoundError:
    print(f'Filen {filename} blev ikke fundet. Starter med en tom liste.')

menu()

