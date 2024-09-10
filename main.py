def mi_funcion_recursiva(repetir):
    retorno = 1
    print(repetir)
    if repetir > 1:
        retorno = mi_funcion_recursiva(repetir - 1)
    return retorno

print(mi_funcion_recursiva(5))