def fibonacci_nth(inteiro):

    anterior = 1
    atual = 1

    contador = 3

    if inteiro == 1 or inteiro == 2:
        enesimo = 1

    else:
        while contador <= inteiro:
            anterior, atual = atual, anterior + atual
            contador += 1

        enesimo = atual

    return enesimo
