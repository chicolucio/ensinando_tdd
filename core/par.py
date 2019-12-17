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
