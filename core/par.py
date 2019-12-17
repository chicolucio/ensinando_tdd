def e_par(inteiro):
    if isinstance(inteiro, int):
        return inteiro % 2 == 0
    else:
        raise TypeError('Deve ser um número inteiro!')
