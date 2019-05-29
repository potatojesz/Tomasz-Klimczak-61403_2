import mLista
import utils


def main():
    should_exit = False
    while should_exit is False:
        try:
            utils.print_start()
            capacity = int(input())
            lista = mLista.MLista(capacity)
            while should_exit is False:
                try:
                    utils.print_menu()
                    option = input()
                    if option == "pisz":
                        lista.pisz()
                    elif option == "dodaj_element":
                        utils.print_value_element()
                        value = int(input())
                        correct = lista.dodaj_element(value)
                        if correct is False:
                            utils.print_error()
                    elif option == "znajdz":
                        utils.print_value_element()
                        value = int(input())
                        print(lista.znajdz(value))
                    elif option == "pobierz":
                        utils.print_index()
                        value = int(input())
                        print(lista.pobierz(value))
                    elif option == "rozmiar":
                        print(lista.rozmiar())
                    elif option == "pojemnosc":
                        print(lista.pojemnosc())
                    elif option == "usun_powtorzenia":
                        utils.print_value_element()
                        value = int(input())
                        lista.usun_powtorzenia(value)
                    elif option == "odwroc":
                        lista.odwroc()
                    elif option == "zwieksz_pojemnosc":
                        utils.print_value()
                        value = int(input())
                        correct = lista.zwieksz_pojemnosc(value)
                        if correct is False:
                            utils.print_error()
                    elif option == "zmniejsz_pojemnosc":
                        utils.print_value()
                        value = int(input())
                        correct = lista.zmniejsz_pojemnosc(value)
                        if correct is False:
                            utils.print_error()
                    elif option == "wyjscie":
                        should_exit = True
                    else:
                        utils.print_error()
                except ValueError:
                    utils.print_error()
        except ValueError:
            utils.print_error()
    utils.print_end()


if __name__ == "__main__":
    main()
