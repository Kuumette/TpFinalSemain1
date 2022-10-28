def menu():
    print("Choix :")
    print("1. Nombre de lignes")
    print("2. Nombre de mots")
    print("3. Nombre de conjonction de coordination")

car = [ 'mais' , 'ou' , 'et' , 'donc' , 'or' , "ni" , 'car' ]
def freq(filename):
   with open(filename) as file:
    text = file.read()
    mais = sum(mot.endswith("mais") for mot in text.split())
    ou = sum(mot.endswith("ou") for mot in text.split())
    et = sum(mot.endswith("et") for mot in text.split())
    donc = sum(mot.endswith("donc") for mot in text.split())
    o = sum(mot.endswith("or") for mot in text.split())
    ni = sum(mot.endswith("ni") for mot in text.split())
    car = sum(mot.endswith("car") for mot in text.split())

    summe = sum([mais, ou, et,donc,o, ni, car])
    print(summe)
    


def nbrsMots(filename):
    nb_chars = nb_words = nb_lines = is_alnum = 0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            nb_lines += 1
            for char in line:
                nb_chars += 1
                if char.isalnum() and not is_alnum:
                    is_alnum = True
                elif is_alnum:
                    nb_words, is_alnum = nb_words + 1, False
    print(nb_words)
    return nb_words

def nbrsLignes(filename):
    nb_lines = 0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            nb_lines += 1

    print(nb_lines)
    return nb_lines


def app(choix):
    if choix == "1":
        nbrsLignes("hello.txt")
    elif choix == "2":
        nbrsMots("hello.txt")
    elif choix == "3":
       freq("hello.txt")


def main():
    menu()
    app(app(choix = input("Choix :")))

if __name__ == '__main__':
    main()
