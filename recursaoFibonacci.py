# FATEC - ESTRUTURAS DE DADOS - PROF. MASANORI
#lru_cache Python 3 => RECURSÃO com biblioteca lru_cache para excluir as repetições:

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(100))

'''
-----------------------------------------------------------------------------------
 Fibonacci recursivo é melhor que o interativo? Não. Por que?
 Porque existe processamentos repetidos.
 Como isso pode ser melhorado? ESTRUTURA DE DADOS
 1-Dicionário que guarda os valores. (no caso usei lru-cache)
 2.Memoria do sistema operacional.
 Das duas, a melhor com certeza é a lru-cache, 
 pois é mais simples e não existe repetição, pois protege regiões críticas
 ----------------------------------------------------------------------------------
 '''