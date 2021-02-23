# FATEC - ESTRUTURAS DE DADOS - PROF. MASANORI
#Recursão para MDC
def mdc(a,b):
    if a % b == 0: return b
    return mdc(b,a%b)