"""
Tema laborator 3 - Problemele 9 si 19
"""


def get_longest_product_is_odd(lst):
    """
    Functia returneaza cea mai lunga secventa cu proprietatea ca
    produsul numerelor din aceasta este prim
    :param lst: lista data -list[int]
    :return: secventa maxima - list[int]
    """
    secventa_maxima_1 = []
    for start in range(len(lst)):
        for end in range(start, len(lst) + 1):
            if if_product_is_odd(lst[start:end]) and len(lst[start:end]) > len(secventa_maxima_1):
                secventa_maxima_1 = lst[start:end]
    return secventa_maxima_1


def if_product_is_odd(lst):
    product = 1
    for numar in lst:
        product = product * numar
    if product % 2 == 1:
        return True
    else:
        return False


def get_longest_concat_digits_asc(lst: list[int]):
    """
    Fuctia returneaza cea mai lunga secventa in care concatenarea numerelor din ea
    are cifrele in ordine crescatoare
    :param lst: lista data - list[int]
    :return: secventa maxima care respecta regula
    """
    secventa_maxima_2 = []
    for start in range(len(lst)):
        for end in range(start , len(lst) + 1):
            if concatenare_cifre_crescatoare(lst[start:end]) and len(lst[start:end]) > len(secventa_maxima_2):
                secventa_maxima_2 = lst[start:end]
    return secventa_maxima_2


def concatenare_cifre_crescatoare(list):
    """
    VOi folosi functia suport "concatenare" care lipeste praactic numerele din lista
    Dupa care voi verifica daca acestea au cifrele in ordine crescatoare
    """
    numar_mare = concatenare(list)
    ultima_cifra = numar_mare%10
    numar_mare = numar_mare // 10
    while numar_mare :
        if numar_mare % 10 > ultima_cifra:
            return False
        ultima_cifra = numar_mare % 10
        numar_mare = numar_mare // 10
    return True


def cate_cifre(n):
    """
    Aflu cate cifre are un numar
    Acest lucru ajuta la concatenarea unor numere
    """
    if n == 0:
        return 1
    cifre = 0
    copien = n
    while copien:
        copien = copien // 10
        cifre = cifre + 1
    return cifre


def concatenare(list):
    """
    Folosesc functie cate_cifre, ajutatoare, utila in concatenarea mai multor numere
    """
    numar_mare = 0
    for numar in list:
        numar_mare = numar_mare * (10**cate_cifre(numar)) + numar
    return numar_mare


def get_longest_concat_is_prime(lst):
    """
    Functia returneaza cea mai lunga secventa in care concatenarea numerelor din aceasta
    este un numar prim
    :param lst: list[int]
    :return: secventa_maxima_3 - secventa maxima care respecta regula - list[int]
    """
    secventa_maxima_3 = []
    for start in range(len(lst)):
        for end in range(start, len(lst) + 1):
            if concatenare_is_prime(lst[start:end]) and len(lst[start:end]) > len(secventa_maxima_3):
                secventa_maxima_3 = lst[start:end]
    return secventa_maxima_3



def concatenare_is_prime(lst: list[int]):
    """
    O fucntie ajutatoare care verifica daca concatenarea numerelor dintr-o lista este numar prim
    Folosesc fuctia concatenare definita mai sus
    """
    numar_mare = concatenare(lst)
    if numar_mare < 2:
        return False
    if numar_mare == 2 :
        return True
    if numar_mare % 2 == 0:
        return False
    for divizor in range(3, int(numar_mare/2)):
        if numar_mare % divizor == 0:
            return False
    return True



def citire_lista_principala():
    lista = []
    lista_string = input('Cititi de la tastatura elementele listei cu spatii intre ele: ')
    numere_string = lista_string.split(' ')
    for numar in numere_string:
        lista.append(int(numar))
    return lista


def test_get_longest_concat_digits_asc():
    assert get_longest_concat_digits_asc([12, 32, 12, 3, 4, 5]) == [12, 3, 4, 5]
    assert get_longest_concat_digits_asc([1, 2]) == [1, 2]
    assert get_longest_concat_digits_asc([98, 454276, 136678, 9411, 1667, 999]) == [1667, 999]


def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([1, 1, 1, 2, 3, 9, 17, 21]) == [3, 9, 17, 21]
    assert get_longest_product_is_odd([1, 2, 848, 298, 457, 12]) == [1]
    assert get_longest_product_is_odd([295, 9347, 93476, 2455433]) == [295, 9347]


def test_get_longest_concat_is_prime():
    assert get_longest_concat_is_prime([3, 0, 3, 0, 1]) == [0, 3]
    assert get_longest_concat_is_prime([12, 24, 10, 1]) == [10, 1]
    assert get_longest_concat_is_prime([1, 12, 24 , 45]) == []


def main():
    while True:
        print('1. Cea mai lunga secventa in care produsul numerelor este impar')
        print('2. Cea mai lunga secventa in care concatenarea numerelor din aceasta'
              ' are cifrele crescatoare')
        print('3. Cea mai lunga secventa in care concatenarea numerelor din aceasta'
              ' este un numar prim')
        print('x. Exit !')
        optiune = input('Alege optiunea : ')
        if optiune == '1':
            lista2 = citire_lista_principala()
            print('Cea mai lunga secventa in care produsul numerelor este impar este:')
            print(get_longest_product_is_odd(lista2))
        elif optiune == '2':
            lista3 = citire_lista_principala()
            print('Cea mai lunga secventa in care concatenarea numerelor din aceasta'
                  'are cifrele crescatoare este: ')
            print(get_longest_concat_digits_asc(lista3))
        elif optiune == '3':
            lista4 = citire_lista_principala()
            print('Cea mai lunga secventa in care concatenarea numerelor din aceasta'
                  'este un numar prim este: ')
            print(get_longest_concat_is_prime(lista4))
        elif optiune == 'x':
            break


test_get_longest_product_is_odd()


test_get_longest_concat_digits_asc()


test_get_longest_concat_is_prime()

main()

