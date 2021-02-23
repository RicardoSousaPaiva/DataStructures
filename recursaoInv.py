# FATEC - ESTRUTURAS DE DADOS - PROF. MASANORI
#Recursão para inverter strigs
def inv(s):
    if len(s) == 0: return ''
    return inv(s [1:]) + s[0]