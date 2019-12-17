def check_inteiro_positivo(funcao):
    def func_wrapper(inteiro):
        if isinstance(inteiro, int) and inteiro >= 0:
            pass
        else:
            raise ValueError('Deve ser inteiro e positivo')
        return funcao(inteiro)
    return func_wrapper


@check_inteiro_positivo
def fatorial_for(inteiro):
    if inteiro == 0 or inteiro == 1:
        resultado = 1
    else:
        resultado = 1
        for i in range(1, inteiro + 1):
            resultado *= i
    return resultado


@check_inteiro_positivo
def fatorial_while(inteiro):
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
    if inteiro == 0 or inteiro == 1:
        resultado = 1
    else:
        resultado = inteiro * fatorial_recursivo(inteiro-1)
    return resultado
