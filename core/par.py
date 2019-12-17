def e_par(inteiro):
    """Função testa se inteiro é par.

    Parameters
    ----------
    inteiro : int
        Os conceitos de par e ímpar só fazem sentido para inteiros.

    Returns
    -------
    bool
        Retorna True ou False

    Raises
    ------
    TypeError
        Retorna TypeError caso não seja inteiro.
    """
    if isinstance(inteiro, int):
        return inteiro % 2 == 0
    else:
        raise TypeError('Deve ser um número inteiro!')


if __name__ == "__main__":
    n = eval(input('Insira um inteiro para testar se é par: '))
    print(e_par(n))

#  TODO Melhorar saída do programa, escrevendo "É par" ou "É ímpar"
# TODO programa com loop infinito, até escrever "sair" por exemplo
