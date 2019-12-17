def fibonacci_nth(posicao):
    """Retorna o enésimo número de uma sequência de Fibonacci

    Parameters
    ----------
    posicao : type
        Posição que se quer da sequência

    Returns
    -------
    int
        Valor do número em tal posição da sequência
    """
    anterior = 1
    atual = 1

    contador = 3

    if posicao == 1 or posicao == 2:
        enesimo = 1

    else:
        while contador <= posicao:
            anterior, atual = atual, anterior + atual
            contador += 1

        enesimo = atual

    return enesimo


# TODO fazer o if main para rodar direto do terminal
