def check_inteiro_positivo(funcao):
    """Decorador para verificar se número é inteiro e maior ou igual a zero.

    Parameters
    ----------
    funcao : function
        Função a ser decorada.

    Returns
    -------
    function
        Função com efeito do decorador

    Raises
    ------
    ValueError
        Erro se não for inteiro e positivo.
    """
    def func_wrapper(inteiro):
        if isinstance(inteiro, int) and inteiro >= 0:
            pass
        else:
            raise ValueError('Deve ser inteiro e positivo')
        return funcao(inteiro)
    return func_wrapper


@check_inteiro_positivo
def fatorial_for(inteiro):
    """Cálculo de fatorial usando for.

    Parameters
    ----------
    inteiro : int
        Número inteiro e positivo

    Returns
    -------
    int
        Fatorial do número fornecido.
    """
    if inteiro == 0 or inteiro == 1:
        resultado = 1
    else:
        resultado = 1
        for i in range(1, inteiro + 1):
            resultado *= i
    return resultado


@check_inteiro_positivo
def fatorial_while(inteiro):
    """Cálculo de fatorial usando while.

    Parameters
    ----------
    inteiro : int
        Número inteiro e positivo

    Returns
    -------
    int
        Fatorial do número fornecido.
    """
    if inteiro == 0 or inteiro == 1:
        resultado = 1
    else:
        resultado = 1
        while inteiro != 1:
            resultado *= inteiro
            inteiro -= 1

    return resultado


@check_inteiro_positivo
def fatorial_recursivo(inteiro):
    """Cálculo de fatorial usando recursividade.

    Parameters
    ----------
    inteiro : int
        Número inteiro e positivo

    Returns
    -------
    int
        Fatorial do número fornecido.
    """
    if inteiro == 0 or inteiro == 1:
        resultado = 1
    else:
        resultado = inteiro * fatorial_recursivo(inteiro-1)
    return resultado
