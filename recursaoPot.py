# FATEC - ESTRUTURAS DE DADOS - PROF. MASANORI
#Recursão para potência
def pot(x,n):
    if n == 0: return 1
    return x * pot( x,n-1)