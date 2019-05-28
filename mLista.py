class MLista:
    def __init__(self, capacity):
        self.lista = []
        self.capacity = capacity

    def pisz(self):
        print("Rozmiar listy: " + str(len(self.lista)))
        print("Pojemnosc listy: " + str(self.capacity))
        print("Elementy: [", end="")
        first = True
        for element in self.lista:
            if first:
                print(element, end="")
                first = False
            else:
                print(", " + str(element), end="")
        print("]")

    def dodaj_element(self, x):
        if len(self.lista) >= self.capacity:
            return False
        else:
            self.lista.append(x)
            return True

    def znajdz(self, x):
        try:
            return self.lista.index(x)
        except ValueError:
            return -1

    def pobierz(self, x):
        try:
            return self.lista[x]
        except IndexError:
            return "Podany index przekracza wielkosc listy."

    def rozmiar(self):
        return len(self.lista)

    def pojemnosc(self):
        return self.capacity

    def usun_powtorzenia(self, x):
        self.odwroc()
        while self.lista.count(x) > 1:
            self.lista.remove(x)
        self.odwroc()

    def odwroc(self):
        self.lista.reverse()

    def zwieksz_pojemnosc(self, x):
        if x < 0:
            return False
        else:
            self.capacity += x
            return True

    def zmniejsz_pojemnosc(self, x):
        if self.capacity < x:
            return False
        else:
            if self.capacity - x < len(self.lista):
                return False
            else:
                self.capacity -= x
                return True
